"""Build the qos.ae site: every page in English (/) and Tamil (/ta/).

    python tools/build.py

Pages are written into site/, next to site/assets/. Each page body uses two
tokens: @R@ is the path back to the site root (for assets), @L@ the root of the
page's own language (for links between pages).
"""
from pathlib import Path

from content_en import EN
from content_ta import TA

SITE = Path(__file__).resolve().parent.parent / "site"
PAGES = ["", "features/", "download/", "docs/", "roadmap/", "community/", "about/"]
MENU = ["features/", "download/", "docs/", "roadmap/", "community/", "about/"]
FINGERPRINT = "6A57FBAEAE589E8B7D1BC7F2758A9E747A6CF66A22603A1718E16F390E944AB8"


def depth(path):
    return path.count("/")


def render(lang, text, other, slug):
    prefix = "" if lang == "en" else "ta/"
    root = "../" * depth(prefix + slug)
    lroot = root + prefix
    other_href = root + ("ta/" if lang == "en" else "") + slug
    page = text["pages"][slug]
    menu = "\n".join(
        f'      <a href="{lroot}{m}"' + (' aria-current="page"' if m == slug else "") + f'>{text["menu"][m]}</a>'
        for m in MENU
    )
    footer_cols = "\n".join(
        f'    <div><h4>{title}</h4><ul>' + "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links) + "</ul></div>"
        for title, links in text["footer"]
    )
    title = text["brand_title"] if slug == "" else f'{page["title"]} · qos'
    html = f"""<!doctype html>
<html lang="{lang}" data-root="{root or './'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{page['description']}">
<link rel="icon" href="@R@assets/qos-icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="@R@assets/qos-icon-192.png">
<link rel="alternate" hreflang="en" href="https://qos.ae/{slug}">
<link rel="alternate" hreflang="ta" href="https://qos.ae/ta/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{page['description']}">
<meta property="og:image" content="https://qos.ae/assets/qos-logo.png">
<link rel="stylesheet" href="@R@assets/site.css">
</head>
<body>

<div class="banner"><div class="wrap"><a href="@L@roadmap/#releases">{text['banner']}</a></div></div>

<nav class="nav">
  <div class="wrap">
    <a class="brand" href="@L@"><img src="@R@assets/qos-icon-192.png" alt="" width="32" height="32">qos</a>
    <div class="menu">
{menu}
    </div>
    <div class="nav-end">
      <a class="lang" href="{other_href}" hreflang="{other}" lang="{other}">{text['other_language']}</a>
      <a class="btn primary small" href="@L@download/">{text['get']}</a>
      <button class="menu-toggle" type="button" aria-expanded="false">{text['menu_button']}</button>
    </div>
  </div>
</nav>

<main>
{page['body']}
</main>

<footer>
  <div class="wrap">
  <div class="foot">
    <div class="about"><img src="@R@assets/qos-icon-192.png" alt="" width="40" height="40"><p>{text['footer_about']}</p></div>
{footer_cols}
  </div>
  <div class="legal"><span>{text['legal']}</span><a href="{other_href}" lang="{other}">{text['other_language']}</a></div>
  </div>
</footer>

<script src="@R@assets/site.js"></script>
</body>
</html>
"""
    html = html.replace("@R@", root).replace("@L@", lroot).replace("@FP@", FINGERPRINT)
    out = SITE / prefix / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")
    return out


def main():
    for lang, text, other in (("en", EN, "ta"), ("ta", TA, "en")):
        for slug in PAGES:
            print(render(lang, text, other, slug).relative_to(SITE.parent))


if __name__ == "__main__":
    main()
