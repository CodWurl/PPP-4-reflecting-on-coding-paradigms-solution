# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    out = []
    for item in array:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
                out.append(item)
                
    return sorted(out)

first_collection=[1,[55,17,12],3, [22,19,35],9,2]
print(flatten_and_sort(first_collection))
print(first_collection)
   

"""
How does this solution ensure data immutability?
    Passes back a different collection than the one passed in
    
Is this solution a pure function?  Why or why not?
    Yes- it does not produce side effects and does not retain state
    
Is this solution a higher order function? Why or why not?
    No-This seems ok
    
Why in particular is functional programming a helpful paradigm when solving this problem?
    Because it is side effect free and because it uses a pure function the result will be consistent and predictable
"""
