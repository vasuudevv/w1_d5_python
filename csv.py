import csv
 
with open('final.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)