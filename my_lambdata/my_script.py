# my_script.py

import numpy as np
from pandas import DataFrame
from my_lambdata.my_mod import enlarge
from my_lambdata.my_mod import decimate
from my_lambdata.my_mod import checknan

print("HELLO")

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df.head())

x = 11
print(enlarge(x))

z = int(input("Please choose a number (e.g. 5): "))
print(decimate(z))
