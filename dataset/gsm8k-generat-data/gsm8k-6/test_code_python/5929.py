def solution():
    # Set up the equation that describes the number of fruits in the bowl
    # Let x be the number of oranges
    # 2 + 2n + x = 12
    # where n is the number of apples (twice the number of bananas)
    
    # Solve for x (the number of oranges)
    n = 2  # since there are 2 bananas and n is twice the number of bananas
    x = 12 - 2 - 2*n
    result = x
    return result

print(solution())