import csv
from textblob import *
from urllib.request import urlopen as ureq
#import f

'''
filename = "CriticsReview.csv"
f = open(filename, "a")
headers="Sentiment\n"
f.write(headers)
f.close()
'''

#code for print 2 nd column of CSV file
with open("CriticsReview.csv","r" or "a") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        try:
            sen = (line[1])
            blob = TextBlob(sen)
            print(blob.sentiment)
            fileadd=(blob.sentiment)

        finally:pass
try :
    csv_file.close()
finally:
    pass
'''
#code for print 2 nd column In CSV file
with open("CriticsReview.csv","w"or"a") as csv_file:
    csv_write = csv.reader(csv_file)
    header="Sentiment\n"
    csv_write.write(header)
    for line in csv_write:
        try:
            sen = (line[2])
            blob = TextBlob(sen)
            col3=(blob.sentiment)
            csv_write.write("," + col3 + "\n")
            #writer = csv.writer("," + col3 + "\n")

        finally:
                pass
    csv_file.close()'''
'''

with open("CriticsReview.csv","a") as csvinput:
    with open("CriticsReview.csv", "w") as csvoutput:

        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            writer.writerow(row+['Berry'])
'''