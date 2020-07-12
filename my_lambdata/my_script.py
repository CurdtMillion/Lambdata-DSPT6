# my_script.py a test script to see if importing
# modules was possible.

import numpy as np
from pandas import DataFrame
from my_lambdata.my_mod import enlarge
from my_lambdata.my_mod import decimate
from my_lambdata.my_mod import checknan
from my_lambdata.my_mod import addrow

print("HELLO")

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df.head())

df2 = addrow(df) # <--- An attempt to try my addrow function
print(df2)

x = 11
print(enlarge(x))

z = int(input("Please choose a number (e.g. 5): "))
print(decimate(z))
