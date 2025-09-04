# make_icons.py
from pathlib import Path
from PIL import Image, ImageColor

SRC = Path("icons/source-1024.png")   # твоя картинка 1024×1024
OUT = Path("icons")
OUT.mkdir(exist_ok=True, parents=True)

BG  = ImageColor.getcolor("#106b2e", "RGB")  # фон (как цвет стола)

def save(img, size, name):
    img.resize((size, size), Image.LANCZOS).save(OUT / name, format="PNG")

base = Image.open(SRC).convert("RGBA")

# PWA
save(base, 192, "icon-192.png")
save(base, 512, "icon-512.png")

# favicon
save(base, 32, "favicon-32.png")
save(base, 16, "favicon-16.png")

# iOS (иконка на Домой)
save(base, 180, "apple-touch-icon.png")

# maskable (Android) — добавим внутренний отступ, чтобы не обрезало углы
pad = int(base.width * 0.14)  # 14% можно увеличить до 0.18 при желании
maskable = Image.new("RGBA", (base.width + pad*2, base.height + pad*2), BG + (255,))
maskable.paste(base, (pad, pad), base)
maskable.resize((512, 512), Image.LANCZOS).save(OUT / "icon-512-maskable.png")

print("Готово. Файлы в папке /icons:")
for p in ["icon-192.png","icon-512.png","icon-512-maskable.png","apple-touch-icon.png","favicon-32.png","favicon-16.png"]:
    print("  -", p)
