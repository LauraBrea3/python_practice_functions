#Problem 1 Write a Python function called max_num()to find the maximum of three numbers.
def max_num(x,y,z):
   return max([x,y,z])

print(max_num(3,17,418))

#Problem 2 Write a Python function called mult_list() to multiply all the numbers in a list.

#Not sure if this counts as a solution for this problem but this is one way I tried it
def mult_list(num):
    if num == 1:
        return 1
    else:
        return (num * mult_list(num-1))
i = 6 
print(mult_list(i))

#This is the second way I found to do it
def mult_lists(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list = [2,4,6,8]
print(mult_lists(list))

#Problem 3 Write a Python function called rev_string() to reverse a string.

def rev_string(a):
    return a[::-1]

txt = rev_string("This is how this sentence looks in reverse")
print(txt)

#Problem 4 Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x):
    if x in range(3,10):
        print ("This number is within range")
    else: 
        print("This number is outside the range provided")

num_within(8)

#Problem 5 Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(x):
    current_row = []
    current_row.append(1)

    if x == 0:
        return current_row
    prev_row = pascal(x - 1)

    for i in range(1, len(prev_row)):
        current = prev_row[i - 1] + prev_row[i]
        current_row.append(current)
    current_row.append(1)

    return current_row

n = 2
tri = pascal(n)
for i in range(len(tri)):
    if i ==(len(tri) - 1):
        print(tri[i])
    else:
        print(tri[i], end=" ")
