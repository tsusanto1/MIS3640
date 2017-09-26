# Exercise 1
#a
sum = 0
for i in range(11):
    sum = sum + i
print(sum)

#b
sum = 0
for i in range (1001):
    sum = sum + i
print(sum)
    

#c
#even
result = 0
for i in range(0, 1001, 2):
    result = result + i
print(result)

#odd 
result = 0
for i in range(1,1001, 2):
    result = result + i
print(result)

# Exercise 2
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#12, 24, 36, 48, 60

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
#12, 12, 12, 12, 12 

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
#1, 12, 1, 12, 1

# Exercise 3
import math
def mysqrt(a):
    x = 10
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x

def test_square_root(n):
    for i in range(1,n):
        mineS = mysqrt(i)
        mathS = math.sqrt(i)
        if i == 1:
            print("a    mysqrt(a)   math.sqrt(a)    diff\n")
            print("-    ---------   ------------    ----\n")
        print(i, "  ", mineS, " ", mathS, " ", mineS-mathS, "\n")

test_square_root(9)