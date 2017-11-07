import csv
print("started")
map = {}
with open(r'import.csv', 'r') as csvToCheck:
    reader = csv.reader(csvToCheck)
    with open(r'c:\temp\output.csv', 'w') as outputCsv:
        writer = csv.writer(outputCsv)
        for row in reader:
            code = row[0].strip()
            if map.has_key(code):
                ref = map[code]
                writer.writerow((code, code))
            else:
                map[code] = code