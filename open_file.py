#!/usr/bin/python3

files = input('Please, enter the file name: ')
"""
# input = files.read()
# print(len(input))

for line in files:
    # line = line.rstrip() # to skip the default new line character at the end of the print function 
    if line.startswith('In'):
        print(line)
"""

try:
    file_name = open(files)
except:
    print('File name error', files)
    quit() # tTo terminate the python program silently without traceback. Useful when you want to stop executing because you detected an error

count = 0
for line in file_name:
    if line.startswith('Friendship'):
        count += 1
    print('There were', count, 'subject lines in', file_name)