# paper-archive

Scan paper bills and records, extract the date and sender with OCR,
and store them in a searchable local database.

**Status:** early development. Tested only with fake sample documents.

## Setup
1. Install Tesseract: `sudo apt install tesseract-ocr tesseract-ocr-por`
2. Create a virtual environment and run `pip install -r requirements.txt`
3. Try it: `python ocr_test.py samples/fake_bill_en.png`

## Privacy
Your scans and database stay on your own machine and are never uploaded.
