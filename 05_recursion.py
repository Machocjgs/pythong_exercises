'''
Exercise 5: Recursion
Goal:
    By using recursion,
    determine the number of iteration it takes for n to reach >= 100 
    with adding 3 in every recursion.
    
    For example:
        from 0 to 100, it takes 35 recursions by adding 3 in every recursion.
        
        inital 0, (1 iteration)
            next -> 0+3=3 (2 iterations)
                next -> 3+3 = 6 (3 iterations)
'''

# Solution

def recursion(k, count=1):
    print(k, count)
    if k >= 100:
        return count
    return recursion(k+3, count+1)

print(recursion(90))