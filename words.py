import numpy as np

#loop 1
def num_letters(num_rows, num_columns):
    return n_rows*n_columns-((n_rows-2)*(n_columns-2))

data = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
n_rows, n_columns = data.shape #3 is n_rows and 13 is the num_columns
assert data[0, 3] == "D"
print("Checking assertions.")
#ASSERTION 1
assert num_letters(4, 13) == 30
print("Checking assertions.") #this worked
#ASSERTION 2

#loop 2
def num_letters(num_rows, num_columns):
    return n_rows*n_columns-((n_rows-2)*(n_columns-2))

data = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
n_rows, n_columns = data.shape #4 is n_rows and 4 is the num_columns
assert num_letters(4, 4) == 12
print("Checking assertions.")#this worked
#ASSERTION 3

#loop 3
def num_letters(num_rows, num_columns):
    return n_rows*n_columns-((n_rows-2)*(n_columns-2))

data = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
n_rows, n_columns = data.shape #4 is n_rows and 6 is the num_columns
assert num_letters(4, 6) == 16
print("Checking assertions.")#this worked
#ASSERTION 4

#loop 4
def num_letters(num_rows, num_columns):
    return n_rows*n_columns-((n_rows-2)*(n_columns-2))

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
n_rows, n_columns = data.shape #7 is n_rows and 6 is the num_columns
assert num_letters(7, 6) == 22
print("Checking assertions.") #this worked
#ASSERTION 5




