# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    
    max2 = max(x, y)
   
    return max2 


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    max_xy = max_of_two(x, y)
    max3 = max(max_xy, z)
    
    return max3 

# x = int(input())
# y = int(input())
# z = int(input())
# print(max_of_two(x, y))
# print(max_of_three(x, y, z))