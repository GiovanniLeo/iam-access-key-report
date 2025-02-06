import csv
import re

def clean_csv(input_file, output_file):
    pattern = re.compile(r'T\d{2}:\d{2}:\d{2}Z')

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = [[pattern.sub('', cell) for cell in row] for row in reader]

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

if __name__ == '__main__':
    # Esempio di utilizzo
    input_csv = 'output-file.csv'  # Sostituisci con il tuo file CSV
    output_csv = 'output-clean.csv'
    clean_csv(input_csv, output_csv)
    print(f"File pulito salvato come {output_csv}")
