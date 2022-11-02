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
print(flatten_and_sort([1,[55,17,12],3, [22,19,35],9,2]))
   

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?

Is this solution a pure function? Why or why not?

Is this solution a higher order function? Why or why not?

Would it have been easier to solve this problem using a different programming style?

Why in particular is functional programming a helpful paradigm when solving this problem?
'''
