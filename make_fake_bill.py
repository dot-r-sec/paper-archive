"""make_fake_bill.py - creates a FAKE utility bill image for testing.
All data below is invented. Never use real documents for tests."""

from pathlib import Path                      # Path: a safe, readable way to handle file paths
from PIL import Image, ImageDraw, ImageFont   # Pillow: create images, draw on them, load fonts

OUTPUT = Path("samples/fake_bill_en.png")     # where the finished image will be saved


def load_font(size):
    """Try a clean system font; fall back to Pillow's built-in one."""
    try:
        # truetype() loads a font file at the requested pixel size
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except OSError:                           # raised if the font file doesn't exist
        return ImageFont.load_default()       # built-in fallback font


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)   # make samples/ if missing, no error if it exists
    img = Image.new("RGB", (1240, 1754), "white")      # blank white page, about A4 size at 150 dpi
    draw = ImageDraw.Draw(img)                         # a "pen" that can draw on that page

    # Each entry is (vertical position, text, font size)
    lines = [
        (100, "Sunshine Electric Company", 56),
        (200, "Statement Date: March 3, 2024", 36),
        (260, "Account Number: ****4821", 36),
        (320, "Billing Period: Feb 1 - Feb 29, 2024", 36),
        (380, "Amount Due: $87.45", 36),
        (440, "Due Date: March 24, 2024", 36),
        (500, "Customer: Jane Doe", 36),
    ]

    for y, text, size in lines:                        # repeat once for every entry in the list
        # text() writes at position (x, y); x is fixed at 100 pixels from the left
        draw.text((100, y), text, fill="black", font=load_font(size))

    img.save(OUTPUT)                                   # write the image file to disk
    print(f"Saved {OUTPUT}")                           # confirm to the user


if __name__ == "__main__":                             # run main() only when executed directly
    main()
