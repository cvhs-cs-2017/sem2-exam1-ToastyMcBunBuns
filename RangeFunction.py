"""Use the range function to print the numbers from 40 to 1 (backwards)"""
for i in range(40, 0, -1):
    print(i)



"""Repeat the exercise but count by 5's"""
for i in range(40, 0, -5):
    print(i)


"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
n = int(input('enter a number: '))
for i in range(0,100,n):
    print (i)
