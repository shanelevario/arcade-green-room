#!/usr/bin/env python3
"""Build index.html from template.html.

Inlines the Arcade brand webfonts and the Firebase web config.
The Firebase config is not a secret: access is controlled by the
Firestore security rules in firestore.rules, not by hiding these keys.

  python3 build.py
  FONTS=/path/to/fonts python3 build.py
"""
import base64, io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.environ.get(
    "FONTS",
    "/Users/Shane/Desktop/OS/.claude/skills/arcade-brand-guidelines/assets/fonts/",
)

def b64(path):
    with open(path, "rb") as fh:
        return base64.b64encode(fh.read()).decode()

tpl = io.open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
tpl = tpl.replace("__LYDIAN_B64__", b64(os.path.join(FONTS, "Lydian.woff")))
tpl = tpl.replace("__AKKURAT_B64__", b64(os.path.join(FONTS, "Akkurat.woff")))

cfg = json.load(io.open(os.path.join(HERE, "fb-config.json"), encoding="utf-8"))
tpl = tpl.replace("__FIREBASE_CONFIG__", json.dumps(cfg))

tpl = tpl.replace("<title>Arcade Green Room</title>\n", "", 1)

doc = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    "<title>Arcade Green Room</title>\n"
    '<link rel="icon" href="data:image/svg+xml,'
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='80' font-size='80'>%F0%9F%AB%98</text></svg>"
    '">\n</head>\n<body>\n' + tpl + "\n</body>\n</html>\n"
)

for bad in ["—", "–", "&mdash;", "&ndash;"]:
    assert bad not in doc, "found banned dash: %r" % bad

io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(doc)
print("built index.html: %d bytes" % len(doc))
