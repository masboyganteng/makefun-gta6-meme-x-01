"""Composite the GTA 6 meme: Vice City scene + make.fun ghost + big captions.

Scene: office worker sprinting down a neon Vice City street, controller held
high, briefcase dropped, coworkers cheering. Ghost: the real make.fun mark
(mark-1024.png, ghost on magenta disc) composited large, flying alongside
the runner -- worked into the scene, not a corner sticker. Captions are drawn
with PIL (never generated) so spelling is exact and text stays huge when the
judge shrinks the picture to 768x480.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "/home/hatch/workspace/makefun-entries/gta6-meme-x-01"
SCENE = f"{BASE}/media-generation-gta6-scene-0-90761957-8cc1-4736-8f89-9721c32a7e08.png"
MARK = f"{BASE}/mark-1024.png"
OUT = f"{BASE}/meme.png"

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def text_center(draw, y, text, font, fill="white", stroke=10):
    w = draw.textlength(text, font=font)
    x = (1920 - w) / 2
    draw.text((x, y), text, font=font, fill=fill,
              stroke_width=stroke, stroke_fill="black")
    return y + font.size


img = Image.open(SCENE).convert("RGB")
assert img.size == (1920, 1280), img.size

# Ghost: large, flying in the open sky at upper left, beside the runner.
ghost = Image.open(MARK).convert("RGBA")
ghost = ghost.resize((380, 380), Image.LANCZOS)
# soft contact shadow under the ghost
shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([95, 795, 445, 845], fill=(0, 0, 0, 90))
shadow = shadow.filter(ImageFilter.GaussianBlur(18))
img = Image.alpha_composite(img.convert("RGBA"), shadow)
img.paste(ghost, (80, 400), ghost)

draw = ImageDraw.Draw(img)
top_font = ImageFont.truetype(FONT, 100)
bot_font = ImageFont.truetype(FONT, 108)
small_font = ImageFont.truetype(FONT, 64)

# Top caption: the 13-year wait, the GTA-specific joke.
text_center(draw, 36, "WAITED 13 YEARS FOR GTA 6", top_font, stroke=12)
# make.fun name right under the ghost (ghost spans x 80..460, centre 270).
mf = "make.fun"
mw = draw.textlength(mf, font=small_font)
draw.text(((270 - mw / 2), 792), mf, font=small_font,
          fill="#ff2fb3", stroke_width=8, stroke_fill="black")

# Bottom caption: launch-day sick day.
text_center(draw, 1010, "IT'S OUT TODAY.", bot_font, stroke=11)
text_center(draw, 1140, "I'M CALLING IN SICK.", bot_font, stroke=11)

img.convert("RGB").save(OUT, "PNG", optimize=True)
print("saved", OUT, Image.open(OUT).size)
