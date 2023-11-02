def solution():
    # Let x be the number of hops taken by the third frog
    x = 1
    
    # Calculate the number of hops taken by the second frog
    y = 2 * x
    
    # Calculate the number of hops taken by the first frog
    z = 4 * y
    
    # Calculate the total number of hops
    total_hops = x + y + z
    
    # Check if the total number of hops is 99
    while total_hops != 99:
        # If not, increase x and recalculate y and z
        x += 1
        y = 2 * x
        z = 4 * y
        total_hops = x + y + z
        
    # Return the number of hops taken by the second frog
    result = y
    return result

print(solution())