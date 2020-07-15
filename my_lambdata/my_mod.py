# my_mod.py 3 modules created by CurdtMillion


def enlarge(n):  # Multiplies by 100
    '''
    Created in class, this multiplies
    a number given by 100.
    '''
    return n * 100


def decimate(n):    # Decreases by 10%
    '''
    Decemates a given number
    '''
    return n - (n * .1)


def checknan(df):   # Checks for NaNs
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

class My_Data_Splitter():
    def __init__(self, df, features, target):
        self.df = df
        self.features = features
        self.target = target
        self.X = df[features]
        self.y = df[target]
    def train_validation_test_split(self,
                                    train_size=0.7, val_size=0.1,
                                    test_size=0.2, random_state=None,
                                    shuffle=True):
        """
        This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or 
        matrices into train, validation, and test subsets.
        Args:
            X (Numpy array or DataFrame): This is the first param.
            y (Numpy array or DataFrame): This is a second param.
            train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        Returns:
            Train, test, and validation dataframes for features (X) and target (y). 
        """
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, shuffle=shuffle)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test
    def print_split_summary(self, X_train, X_val, X_test):
        print('######################## TRAINING DATA ########################')
        print(f'X_train Shape: {X_train.shape}')
        display(X_train.describe(include='all').transpose())
        print('')
        print('######################## VALIDATION DATA ######################')
        print(f'X_val Shape: {X_val.shape}')
        display(X_val.describe(include='all').transpose())
        print('')
        print('######################## TEST DATA ############################')
        print(f'X_test Shape: {X_test.shape}')
        display(X_test.describe(include='all').transpose())
        print('')
Collapse

if __name__ == "__main__":

    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number (e.g. 5): "))
    print(enlarge(y))

    