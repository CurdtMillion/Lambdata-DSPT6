# my_mod.py 3 modules created by CurdtMillion
import pandas as pd
import numpy as np


def enlarge(number: float) -> float:
    '''
    Created in class, this multiplies
    a number given by 100.
    '''
    return number * 100


def decimate(number: float) -> float:
    '''
    Decimates a given number
    '''
    return number - (number * .1)


def checknan(df):
    '''
    Checks if a given DataFrame contains
    NaN values. Will print the DataFrame
    with true and false
    '''
    print(df.isnull())


def addrow(df):
    '''
    Creates a new row in the previously
    made DataFrame containing the
    numbers 4 and 7
    '''
    new_row = {'a': 4, 'b': 7}
    print(df.append(new_row, ignore_index=True))

if __name__ == "__main__":

    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number (e.g. 5): "))
    print(enlarge(y))
