from pathlib import Path
import csv

text_path = Path('text')


def text_before_references(txt):
    lines = txt.splitlines()
    first_ref = -1
    last_ref = -1
    for i, line in enumerate(lines):
        line = line.strip()
        if (line.endswith("References.") or line.endswith("REFERENCES") or line.endswith("References") or line.endswith("REFERENCES.") or line.endswith("LITERATURE  CITED.")):
            #if first_ref != -1:
            #    raise RuntimeError(f"Found duplicate reference section at line {first_ref} and {i}")
            if first_ref == -1:
                first_ref = i
            last_ref = i
    if last_ref == -1:
        raise RuntimeError("Failed to find reference section")
    return ' '.join(lines[:last_ref])


def main():
    with open('out.csv', 'w', encoding="utf-8") as outf:
        out = csv.writer(outf, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
        out.writerow(['DOI', 'Abstract'])
        files = list(text_path.glob('*.txt'))
        files.sort()
        for text_file in files:
            print(f"Extracting text from {text_file}")
            with open(text_file, "r", encoding="utf-8") as f:
                txt = f.read()
            txt = txt.replace('\00', ' ')
            txt = txt.replace('', ' ')
            txt = txt.replace('', ' ')
            #txt = txt.replace(',', '.')
            try:
                words = text_before_references(txt)
            except RuntimeError as e:
                print(f"Failed to extract text from {text_file}: {e}")
                continue
            out.writerow([text_file.stem, words])


main()