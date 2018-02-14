#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from ruffus import *
import csv

starting_file = ['data.csv']

def read_csv(file_obj):
    data = []
    with open(file_obj) as f:
        reader = csv.reader(file_obj)
        for row in reader:
            for num in row:
                data.append(int(num))
    return data

def write_csv(data, file_obj):
    with open(file_obj, 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            for num in line:
                writer.writerow(num)
    
#
# STAGE 1 - Read in file and multiply numbers by 100
#

@transform(starting_file,
            suffix(".csv"),
            ".csv")
def read_multiply(input_file, output_file):
    data = []

    with open(input_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for num in row:
                data.append(int(num))

    transformed = [x*100 for x in data]
    print(transformed)
    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')   
        for i in transformed:
            writer.writerow(str(i))
#
# STAGE 2 - Add 15 to the numbers
#

@transform(read_multiply,
            suffix(".csv"),
            ".csv")

def add_num(input_file, output_file):

    data = []
    with open(input_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for num in row:
                nums = int(num)
                data.append(nums)
    
    transformed = [x+15 for x in data]
    print(transformed)

    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(transformed)):
            writer.writerow(str(i))

    
pipeline_run()
