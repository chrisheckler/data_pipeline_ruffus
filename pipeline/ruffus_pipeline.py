#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from ruffus import *
import csv

starting_file = ['data.csv']

#
# Helper functions to read and write csv
#

def read_csv(input_file):
    data = []
    with open(input_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data = [int(num) for num in row]
    return data

def write_csv(data, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)

#
# STAGE 1 - Read in file and multiply numbers by 100
#

@transform(starting_file,
            suffix(".csv"),
            ".csv")
def read_multiply(input_file, output_file):
    data = read_csv(input_file)

    transformed = [x*100 for x in data]
    print(transformed)
    
    write_csv(transformed, output_file)
#
# STAGE 2 - Add 15 to the numbers
#

@transform(read_multiply,
            suffix(".csv"),
            ".csv")

def add_num(input_file, output_file):

    data = read_csv(input_file)
    
    transformed = [x+15 for x in data]
    print(transformed)

    write_csv(transformed, output_file)
    
pipeline_run()
