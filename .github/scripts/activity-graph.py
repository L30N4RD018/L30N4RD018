#!/usr/bin/env python3
"""Genera el SVG del grafico de actividad de contribuciones.

Reemplaza a github-readme-activity-graph.vercel.app, que quedo deshabilitado de
forma permanente (HTTP 402, x-vercel-error: DEPLOYMENT_DISABLED). Los datos
salen de la GraphQL de GitHub y el SVG se dibuja aca mismo, asi que el job no
depende de ningun servicio de terceros.

Solo usa la stdlib: en el runner no hace falta instalar nada.
"""

import argparse
import datetime as dt
import json
import math
import os
import sys
import urllib.error
import urllib.request

GRAPHQL = "https://api.github.com/graphql"

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

# Stack del sistema: camo proxea el SVG pero no carga fuentes externas, asi que
# cualquier @font-face quedaria en el fallback igual.
FONT = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"

WIDTH, HEIGHT = 840, 280
PAD_L, PAD_R, PAD_T, PAD_B = 48, 24, 56, 40
PLOT_W = WIDTH - PAD_L - PAD_R
PLOT_H = HEIGHT - PAD_T - PAD_B
BASELINE = PAD_T + PLOT_H
DIVISIONS = 4


def fetch_days(login, token, days):
    """Devuelve [(date, count)] de los ultimos `days` dias, en orden."""
    to = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    frm = (to - dt.timedelta(days=days - 1)).replace(hour=0, minute=0, second=0)
    payload = json.dumps(
        {
            "query": QUERY,
            "variables": {
                "login": login,
                "from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "to": to.strftime("%Y-%m-%dT%H:%M:%SZ"),
            },
        }
    ).encode()

    req = urllib.request.Request(
        GRAPHQL,
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-assets-activity-graph",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            body = json.load(res)
    except urllib.error.HTTPError as exc:
        sys.exit(f"GraphQL HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')[:500]}")
    except urllib.error.URLError as exc:
        sys.exit(f"No se pudo contactar la API de GitHub: {exc.reason}")

    # La GraphQL responde 200 con `errors` cuando el token no alcanza; sin este
    # chequeo el fallo se veria como un grafico plano en vez de como un error.
    if body.get("errors"):
        sys.exit("GraphQL: " + json.dumps(body["errors"])[:500])
    user = (body.get("data") or {}).get("user")
    if not user:
        sys.exit(f"GraphQL no devolvio datos para el usuario {login!r}")

    weeks = user["contributionsCollection"]["contributionCalendar"]["weeks"]
    # El calendario viene por semanas completas, asi que desborda la ventana
    # pedida por ambos extremos; se recorta a los ultimos `days` dias.
    all_days = [(d["date"], d["contributionCount"]) for w in weeks for d in w["contributionDays"]]
    all_days.sort()
    return all_days[-days:]


def nice_axis(vmax):
    """Techo y paso del eje Y, siempre enteros para que las etiquetas cierren."""
    vmax = max(int(vmax), 1)
    if vmax <= DIVISIONS:
        return vmax, 1
    step = int(math.ceil(vmax / DIVISIONS))
    return step * DIVISIONS, step


def monotone_tangents(xs, ys):
    """Tangentes de Fritsch-Carlson: curva suave que no se pasa de los datos.

    Un Catmull-Rom normal sobrepasaria en series con picos (0, 0, 15, 0) y el
    area terminaria por debajo de la linea base.
    """
    n = len(xs)
    slopes = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [0.0] * n
    m[0], m[-1] = slopes[0], slopes[-1]
    for i in range(1, n - 1):
        m[i] = 0.0 if slopes[i - 1] * slopes[i] <= 0 else (slopes[i - 1] + slopes[i]) / 2
    for i in range(n - 1):
        if slopes[i] == 0:
            m[i] = m[i + 1] = 0.0
            continue
        a, b = m[i] / slopes[i], m[i + 1] / slopes[i]
        s = a * a + b * b
        if s > 9:
            t = 3.0 / math.sqrt(s)
            m[i], m[i + 1] = t * a * slopes[i], t * b * slopes[i]
    return m


def curve(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    m = monotone_tangents(xs, ys)
    d = [f"M{xs[0]:.2f},{ys[0]:.2f}"]
    for i in range(len(points) - 1):
        dx = (xs[i + 1] - xs[i]) / 3.0
        d.append(
            f"C{xs[i] + dx:.2f},{ys[i] + m[i] * dx:.2f}"
            f" {xs[i + 1] - dx:.2f},{ys[i + 1] - m[i + 1] * dx:.2f}"
            f" {xs[i + 1]:.2f},{ys[i + 1]:.2f}"
        )
    return "".join(d)


def hex_color(value):
    return value if value.startswith("#") else "#" + value


def render(days, title, title_color, axis_color, line_color, area_color):
    counts = [c for _, c in days]
    top, step = nice_axis(max(counts))
    n = len(days)
    dx = PLOT_W / (n - 1) if n > 1 else 0

    def x_of(i):
        return PAD_L + i * dx

    def y_of(v):
        return BASELINE - (v / top) * PLOT_H

    points = [(x_of(i), y_of(c)) for i, c in enumerate(counts)]
    line = curve(points)
    area = f"{line}L{points[-1][0]:.2f},{BASELINE}L{points[0][0]:.2f},{BASELINE}Z"

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="{title}">',
        "<defs>",
        f'<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{area_color}" stop-opacity="0.38"/>'
        f'<stop offset="100%" stop-color="{area_color}" stop-opacity="0.02"/>'
        "</linearGradient>",
        "</defs>",
        f'<text x="{PAD_L}" y="34" font-family="{FONT}" font-size="18" font-weight="600" '
        f'fill="{title_color}">{title}</text>',
    ]

    # Grilla horizontal + etiquetas del eje Y.
    for v in range(0, top + 1, step):
        y = y_of(v)
        out.append(
            f'<line x1="{PAD_L}" y1="{y:.2f}" x2="{PAD_L + PLOT_W}" y2="{y:.2f}" '
            f'stroke="{axis_color}" stroke-opacity="0.22" stroke-width="1"/>'
        )
        out.append(
            f'<text x="{PAD_L - 10}" y="{y + 4:.2f}" text-anchor="end" font-family="{FONT}" '
            f'font-size="11" fill="{axis_color}" fill-opacity="0.85">{v}</text>'
        )

    out.append(f'<path d="{area}" fill="url(#area)"/>')
    out.append(
        f'<path d="{line}" fill="none" stroke="{line_color}" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    for px, py in points:
        out.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="2.6" fill="{line_color}"/>')

    # Etiquetas del eje X: ~6 fechas repartidas, siempre con la primera y la
    # ultima. Formato dd/mm, que se lee igual en el README en ingles y en el de
    # espanol.
    ticks = 6 if n >= 6 else n
    idxs = sorted({round(i * (n - 1) / (ticks - 1)) for i in range(ticks)}) if ticks > 1 else [0]
    for i in idxs:
        date = dt.date.fromisoformat(days[i][0])
        anchor = "start" if i == 0 else "end" if i == n - 1 else "middle"
        out.append(
            f'<text x="{x_of(i):.2f}" y="{BASELINE + 22:.2f}" text-anchor="{anchor}" '
            f'font-family="{FONT}" font-size="11" fill="{axis_color}" fill-opacity="0.85">'
            f"{date:%d/%m}</text>"
        )

    out.append("</svg>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--username", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--title", default="Contribution Graph")
    ap.add_argument("--title-color", default="0969da")
    ap.add_argument("--axis-color", default="57606a")
    ap.add_argument("--line-color", default="0969da")
    ap.add_argument("--area-color", default="0969da")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("Falta GITHUB_TOKEN en el entorno")
    if args.days < 2:
        sys.exit("--days tiene que ser al menos 2")

    days = fetch_days(args.username, token, args.days)
    if len(days) < 2:
        sys.exit(f"La API devolvio {len(days)} dia(s); no alcanza para dibujar la serie")

    svg = render(
        days,
        args.title,
        hex_color(args.title_color),
        hex_color(args.axis_color),
        hex_color(args.line_color),
        hex_color(args.area_color),
    )
    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(svg + "\n")
    total = sum(c for _, c in days)
    print(f"ok  {args.output}  ({len(days)} dias, {total} contribuciones)")


if __name__ == "__main__":
    main()
