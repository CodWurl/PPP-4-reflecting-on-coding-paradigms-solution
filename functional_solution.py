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
   

