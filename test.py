import csv

with open('D:\\HDF\\Abhilash\\IB MAIZE.csv') as fin:
    with open('D:\\HDF\\Abhilash\\IB MAZE.txt', 'w', newline='') as fout:
        reader = csv.DictReader(fin, delimiter=',')
        writer = csv.DictWriter(fout, reader.fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(reader)