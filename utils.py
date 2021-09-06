import csv

def write_csv(fields,file,filename='final_dataset.csv'): # manually writting the csv files.
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(file)

def read_csv(filename): # manually reading the csv files.
    rows = []
    with open(filename, 'r') as csvfile:
        i =1
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        for row in csvreader:
            if len(row):
                rows.append(row)
                i+=1
    print(i)
    return rows,fields

