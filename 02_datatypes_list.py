'''
Exercise 2: Python datatypes

Goal 1: List comprehension
    Using list comprehension, create a list from 1 until 15 and store as initial_set.

Goal 2: Assign value to index is array using append
    By looping initial_set, copy the values BUT check if it is divisible by 3.
    If so, instead of having the value, store as "Marker".
    Store this as initial_set_copy.
    
    Sample output:
        [1,2,"marker", 4,5,"marker",...]

Goal 3: Using Set and builtin methods
Get the length of of unique values of list: initial_set_copy

Bonus points:
    1. using list comprehension, create another list from intial_set for all items divisible by 2

'''
# SOLUTION
initial_set = [x for x in range(1,15)]
initial_set_copy = []
for i in initial_set:
    if i % 3 == 0:
        initial_set_copy.append("marker for 3")
    else:
        initial_set_copy.append(i)

print("Length of unique values: ", len(set(initial_set_copy)))

print([x for x in initial_set if x % 2 == 0])
