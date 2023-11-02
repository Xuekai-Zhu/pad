def solution():
    total_toys = 120
    larger_pile = 0
    smaller_pile = 0
    
    # Set up equations
    # larger_pile + smaller_pile = total_toys
    # larger_pile = 2 * smaller_pile
    
    # Substitute the second equation into the first to solve for smaller_pile
    smaller_pile = total_toys/(2+1)
    
    # Use the second equation to solve for larger_pile
    larger_pile = 2 * smaller_pile
    
    result = larger_pile
    return result

print(solution())