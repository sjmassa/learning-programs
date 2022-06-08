
import sys
import csv
import re
import os

def test_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        print(f'Could not read '+sys.argv[1])
    try:
        open(sys.argv[2])
    except FileNotFoundError:
        print(f'Could not read '+sys.argv[2])

def remove_quotes(infile):
    with open(infile) as infile:
        with open('temp.csv', 'w') as writefile:
            for line in infile:
                for char in line:
                    if char == '"' or char == ' ':
                        char = ''
                        writefile.write(char)
                    else:
                        writefile.write(char)

def rearrange_csv(outfile):
    with open(outfile, 'a') as writefile:
        writer = csv.writer(writefile)
        header = ['first', 'last', 'house']
        writer.writerow(header)
        with open('temp.csv') as infile:
            reader = csv.reader(infile, delimiter=',')
            #Skips header.
            next(reader)
            for line in reader:
                print(line)
                writer.writerow((line[1], line[0], line[2]))

def main(infile, outfile):
    test_arguments()
    remove_quotes(infile)
    rearrange_csv(outfile)
    os.remove('temp.csv')

main(sys.argv[1], sys.argv[2])
