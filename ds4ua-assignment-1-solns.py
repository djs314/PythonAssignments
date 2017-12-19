## File: ds4ua-assignment-1-solns.py
## Topic: Assignment 1 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5
  
  
mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]


## A1.

(2**521 - 1) % 10000

"""
# A1
7151
"""


## A2.

mylist01[6] * mylist01[12] * mylist02[3]

"""
# A2
-75
"""


## A3.

mylist02[4:9]

"""
# A3
[-5, -2, 4, 6, 7]
"""


## A4.

longlist = mylist01 + mylist02
longlist.sort()
longlist[7:19]
longlist = mylist01 + mylist02 # Reset longlist for later problems

"""
# A4
[-3, -3, -2, -2, 0, 0, 1, 2, 2, 2, 3, 3]
"""


## A5.

longlist.count(8)

"""
# A5
3
"""


## A6.

newlist = list(mylist01)
newlist.remove(3)
newlist.remove(3)
print(newlist)

"""
# A6
[2, 5, 4, 9, 10, -3, 5, 5, -8, 0, 2, 8, 8, -2, -4, 0, 6]
"""


## A7.

mylist02[::-3]

"""
# A7
[1, 13, 9, 6, -5, -3]
"""


## A8.

longlist[2::5]

"""
# A8
[4, 5, 3, 0, -5, 7, 13]
"""


mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]


## B1.

s = 0
for x in mylist01:
    s = s + x**3
print(s)

"""
# B1
2867
"""


## B2.

mylist03 = 15*[0]
for i in range(15):
    mylist03[i] = mylist01[i] * mylist02[i]
print(mylist03)

"""
# B2
[-14, -15, 32, -45, -50, 6, 20, 30, 21, -40, 0, 20, 6, 104, -96]
"""


## B3.

n = len(mylist02)
s = 0
for x in mylist02:
    s = s + x
print(s/n)

"""
# B3
1.588235294117647
"""


mylist01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
mylist02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1]
mylist03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = mylist01 + mylist02 + mylist03


## C1.

c = 0
for x in biglist:
    if x > 4:
        c = c + 1
print(c)

"""
# C1
23
"""


## C2.

c = 0
for x in biglist:
    if x >= -1 and x <= 3:
        c = c + 1
print(c)

"""
# C2
15
"""


## C3.

mylist04 = []
for x in biglist:
    if (x % 3) != 0:
        mylist04.append(x)
print(mylist04)

"""
# C3
[2, 5, 4, 10, 5, 5, -8, 2, 8, 8, -2, -4, -7, 8, -5, -5, -2, 4, 7, #new line, couldn't print
5, 10, 2, 13, -4, 1, 2, -5, 7, -2, 2, 8, 7, 2, -2, 5, 5]
"""