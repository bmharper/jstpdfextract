from pathlib import Path
import os
import subprocess
#import shutil

pdf_path = Path('pdf')
text_path = Path('text')

text_path.mkdir(exist_ok=True)

pdf2txt = "pdf2txt.py"

if os.name == 'nt':
    # Find absolute location of pdf2txt.py, which is necessary on windows
    pdf2txt = subprocess.run(["where", "pdf2txt.py"], stdout=subprocess.PIPE).stdout.decode().strip()
    if pdf2txt == "":
        raise RuntimeError("Failed to find pdf2txt.py (have you run 'pip install -r requirements.txt'?)")

files = list(pdf_path.glob('*.pdf'))
files.sort()
for pdf_file in files:
    txt_file = text_path / (pdf_file.stem + ".txt")
    if txt_file.exists():
        print(f"{txt_file} already exists, skipping")
        continue
    print(f"Extracting text from {pdf_file}")
    args = ["-o", txt_file, pdf_file]
    if os.name == "nt":
        subprocess.run(["python", pdf2txt] + args)
    else:
        subprocess.run([pdf2txt] + args)
