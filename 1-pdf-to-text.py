from pathlib import Path
import subprocess

pdf_path = Path('pdf')
text_path = Path('text')

text_path.mkdir(exist_ok=True)

files = list(pdf_path.glob('*.pdf'))
files.sort()
for pdf_file in files:
    print(f"Extracting text from {pdf_file}")
    subprocess.run(["pdf2txt.py", "-o", str(text_path / pdf_file.stem) + ".txt", pdf_file])
