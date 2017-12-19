## File: ds4ua-assignment-3-solns.py
## Topic: Assignment 3 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import numpy as np # Load NumPy
arr1 = np.array([[2,5,3,-1,0,1,-6,8,1,-9],[-1,3,4,2,0,1,2,7,8,-1],
                [3,0,-2,-2,5,4,8,-1,0,2],[3,3,-3,2,4,5,1,9,8,6],
                [1,1,0,2,-3,-2,4,-7,0,-9],[0,1,7,8,-5,-4,0,2,5,-9]])

## A.a

arr1_slice = arr1[1:3] # Extract the submatrix
arr1_slice

"""
# A.a
array([[-1,  3,  4, ...,  7,  8, -1],
       [ 3,  0, -2, ..., -1,  0,  2]])
"""

## A.b

arr1[arr1 < -5] # Entries of arr1 less than -5

"""
# A.b
array([-6, -9, -7, -9, -9])
"""

## A.c

(arr1 > 3).sum() # Number of entries of arr1 greater than 3

"""
# A.c
17
"""

## A.d

arr1[arr1 <= -2].mean() # Mean of entries of arr1 that are less than or equal to -2

"""
# A.d
-5.08333333333333
"""

## A.e

arr1_even = arr1[(arr1 % 2) == 0] # Extract the even entries
(arr1_even**2).sum() # Add the squares of the even entries

"""
# A.e
512
"""

## A.f

arr1_pos = (arr1 > 0).sum() # Number of positive entries
arr1_large = (arr1 > 3).sum() # Number of entries greater than 3
arr1_large/arr1_pos # Report the proportion

"""
# A.f
0.47222222222222221
"""

arr2 = np.arange(-20,28,2)
arr2 = arr2.reshape((4,6))
arr3 = np.arange(-20,12)
arr3 = arr3.reshape((8,4))

## B.a

arr2_sub = arr2[[0,3]][:,[1,4]] # Extract the submatrix
print('The mean of the entires is %f.' % arr2_sub.mean()) # Report the mean
print('The standard deviation of the entries is %f.' % arr2_sub.std()) # Report the standard deviation

"""
# B.a
The mean of the entires is 3.000000.
The standard deviation of the entries is 18.248288.
"""

## B.b

arr2_tripleplus1 = 3 * arr2 + 1 # Triple arr2 and add 1, and store in arr2_tripleplus1
np.where(arr2_tripleplus1 % 2 == 0, 0, arr2_tripleplus1) # Replace the even values with 0 and print

"""
# B.b
array([[-59, -53, -47, -41, -35, -29],
       [-23, -17, -11,  -5,   1,   7],
       [ 13,  19,  25,  31,  37,  43],
       [ 49,  55,  61,  67,  73,  79]])
"""

## B.c

arr3_slice = arr3[[1,6]] # Extract rows 1 and 6
arr3_slice.T # Print the transpose

"""
# B.c
array([[-16,   4],
       [-15,   5],
       [-14,   6],
       [-13,   7]])
"""

## B.d

arr3_replaced = np.where((arr3 < 0) & (arr3 % 2 == 1), 0, arr3) # Replace the odd negative
# entries and store in arr3_replaced
arr3_replaced.mean(axis=1) # Report the mean of each row

"""
# B.d
array([-9.5, -7.5, -5.5, -3.5, -1.5,  1.5,  5.5,  9.5])
"""

## B.e

np.intersect1d(arr2, arr3) # The intersection of arr2 and arr3

"""
# B.e
array([-20, -18, -16, ...,   6,   8,  10])
"""

## B.f

np.setdiff1d(arr3, arr2) # The entires of arr3 that are not in arr2

"""
# B.f
array([-19, -17, -15, ...,   7,   9,  11])
"""

## C1.i

def grade(average):
    if (average >= 90) and (average <= 100): # If the average is in the 90's, return 'A'
        return('A')
    elif (average >= 80) and (average < 90): # If the average is in the b0's, return 'B'
        return('B')
    elif (average >= 70) and (average < 80): # If the average is in the 70's, return 'C'
        return('C')
    elif (average >= 60) and (average < 70): # If the average is in the 60's, return 'D'
        return('D')
    elif (average >= 0) and (average < 60): # If the average is less than 60, return 'F'
        return('F')
    else: # If the average is not between 0 and 100, return an error message
        return('Invalid')

## C1.ii

grades = [99, 73, 60, 91, 93, 92, 68, 55, 60, 79, 79, 92, 51, 78, 68, 90, 99,
       62, 58, 76, 78, 65, 92, 83, 95, 82, 92, 85, 83, 65, 85, 61, 69, 72,
       63, 79, 59, 63, 85, 97]
gradelist = [] # An empty list to hold the letter grades
for g in grades:
    letter_grade = grade(g) # Convert each number in grades to a letter grade
    gradelist.append(letter_grade) # Add the letter grade to the list
print(gradelist) # Print the letter grades

"""
# C1.ii
['A', 'C', 'D', 'A', 'A', 'A', 'D', 'F', 'D', 'C', 'C', 'A', 'F', 'C', 'D', 'A', 'A',
'D', 'F', 'C', 'C', 'D', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'D', 'B', 'D', 'D', 'C',
'D', 'C', 'F', 'D', 'B', 'A']
"""
