#!/usr/bin/env python3

while True:
    try:
        x = int(input('Please, enter a number: '))
        break
    except ValueError:
        print('Oops, Invalid number. Try again...')