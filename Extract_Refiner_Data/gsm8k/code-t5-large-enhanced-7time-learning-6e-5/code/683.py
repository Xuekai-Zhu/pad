def solution():
    
    # Let x be the age of one triplet
    # Then the age of one twin is x + 7
    # The sum of their ages is 44: x + (x + 7) = 44
    # Simplifying, we get: 2x + 7 = 44
    # Solving for x, we get:
    twin_age = (44 - 7) / 2

    # Display the age of one twin
    result = twin_age
    return result

print(solution())