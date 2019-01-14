import csv
from textblob import *
from urllib.request import urlopen as ureq
import f
import ftech
'''

with open('CriticsReview.csv', 'r') as csvfile, open('CriticsReview.csv', 'w') as outputfile:

    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)

    for row in reader:
        sentence = row[0]
        blob = TextBlob(sentence)
        new_row = [sentence, float(blob.sentiment.polarity)]

    writer.writerow(new_row)
    '''
with open('CriticsReview.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            csv_reader.write(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            pass
    print(f'Processed {line_count} lines.')
    csv_reader.write(f'Processed {line_count} lines.')