"""ocr_test.py - reads one image with Tesseract and prints text + confidence."""

import sys                                   # sys: lets us read command-line arguments
from pathlib import Path                     # Path: safe handling of file paths
from PIL import Image                        # Pillow: opens the image file
import pytesseract                           # bridge between Python and the Tesseract program
from pytesseract import Output               # Output.DICT = ask for results as a dictionary


def read_image(path, lang="eng+por"):
    """Return (text, average_confidence) for one image."""
    img = Image.open(path)                   # load the image from disk
    text = pytesseract.image_to_string(img, lang=lang)    # run OCR, get plain text back
    data = pytesseract.image_to_data(img, lang=lang, output_type=Output.DICT)  # per-word details

    # data["conf"] holds one confidence number per detected item; data["text"] holds the word.
    # Tesseract uses -1 for items that aren't real words, so we skip those and blank words.
    confs = [float(c) for c, w in zip(data["conf"], data["text"])
             if w.strip() and float(c) >= 0]

    # Average the word confidences; if no words were found, report 0.0
    avg = sum(confs) / len(confs) if confs else 0.0
    return text, avg


def main():
    if len(sys.argv) != 2:                   # we expect exactly one argument: the image path
        print("Usage: python ocr_test.py <image>")
        sys.exit(1)                          # exit with an error code

    path = Path(sys.argv[1])                 # turn the argument into a Path object
    if not path.is_file():                   # stop early if the file doesn't exist
        print(f"File not found: {path}")
        sys.exit(1)

    text, avg = read_image(path)
    print(text)                              # the recognized text
    print(f"Average confidence: {avg:.1f}/100")   # .1f = one decimal place


if __name__ == "__main__":                   # run main() only when executed directly
    main()
