def solution():
    """Henry went to the beach and picked up 17 perfect shells 
    and 52 broken shells. Out of those 52 broken shells, half of 
    them were spiral. Out of the 17 perfect shells, 12 of them 
    were not spiral. How many more broken spiral shells were there 
    than perfect spiral shells?"""
    
    # Find the number of broken spiral shells
    broken_spiral_shells = 52 / 2
    
    # Find the number of perfect spiral shells
    perfect_spiral_shells = 17 - 12
    
    # Find the difference between number of broken and perfect spiral shells
    difference = broken_spiral_shells - perfect_spiral_shells

    result = difference
    return result

print(solution())