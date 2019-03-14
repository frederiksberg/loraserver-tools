import csv

def read_csv(file):
    with open(file, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')
        return [row for row in rows]