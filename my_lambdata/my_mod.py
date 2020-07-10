# my_mod.py


def enlarge(n): # Multiplies by 100
    return n * 100

def decimate(n):    # Decreases by 10%
    return n - (n * .1)

def checknan(df):   # Checks for NaNs
    print(df.isnull())

def addrow(df):
    print(df.loc[-1] = np.random.randint(1, 10, size=len(df)))

if __name__ == "__main__":
    
    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number (e.g. 5): "))
    print(enlarge(y))
