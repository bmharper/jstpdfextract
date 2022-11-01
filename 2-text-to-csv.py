from pathlib import Path
import csv

text_path = Path('text')


def text_before_references(txt):
    lines = txt.splitlines()
    first_ref = -1
    for i, line in enumerate(lines):
        if (line.endswith("References.") or line.endswith("REFERENCES") or line.endswith("References") or line.endswith("REFERENCES.") or line.endswith("LITERATURE  CITED.")):
            if first_ref != -1:
                raise RuntimeError(f"Found duplicate reference section at line {first_ref} and {i}")
            first_ref = i
    if first_ref == -1:
        raise RuntimeError("Failed to find reference section")
    return ' '.join(lines[:first_ref])


def main():
    with open('out.csv', 'w') as outf:
        out = csv.writer(outf, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
        out.writerow(['DOI', 'Abstract'])
        files = list(text_path.glob('*.txt'))
        files.sort()
        for text_file in files:
            print(f"Extracting text from {text_file}")
            with open(text_file) as f:
                txt = f.read()
            txt = txt.replace('\00', ' ')
            txt = txt.replace('', ' ')
            txt = txt.replace('', ' ')
            #txt = txt.replace(',', '.')
            words = text_before_references(txt)
            out.writerow([text_file.stem, words])


main()