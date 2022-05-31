'''
Exercise 4: Python functions

Goal 1: Create a function
    Create a function that accepts a string.
    Return the string but reverersed.
    example:
        input: truck
        returns: kcurt
    Create a document for your function!!!
    
Goal 2: Default values
    Modify the first function to have a default value for the parameter.
    So that we can call the function without passing an argument
    
Goal 3: Function with arbitrary parameters
    Create a function that checks the arguments if it contains a string
    print the string if it is found, otherwise, print that no string is found.
    
Bonus points: 
    Using built in function, check if [1,2,3,4,"5"] contains a string.
    simply print True if contains true. False if otherwise
'''

# Solution
def string_reverse(target="hello world!"):
    '''
        Accepts a string 
        @target: string to be reversed
        @returns: Reversed format of the string
    '''
    return target[::-1]

print(string_reverse("target"))
print(string_reverse())

def string_checker(*args):
    for i in args:
        if isinstance(i, str):
            print(i, "is string!")
            return
    else:
        print("No string is found")
        
string_checker(1,2,3,4,"5")

print(
    any([isinstance(i,str) for i in [1,2,3,4,"5"]])
)