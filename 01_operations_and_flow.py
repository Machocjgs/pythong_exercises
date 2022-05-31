'''
Exercise 1: Operations and Flow controls
Using range, 
    1. create a loop that prints from 0 - 20 and if it is odd or even.
    2. Every second odd number, display a message: "Second Even"
Bonus points:
    have it print "Job is done" after the loop 
    but it should be somehow connected to the for loop
'''

# Solution:
print("Hello World")
for i in range(0,20):
    if i % 2 == 0:
        print(i, "is Even!")
    else:
        print(i, "is Odd!")
else:
    print("Job is done!")
    