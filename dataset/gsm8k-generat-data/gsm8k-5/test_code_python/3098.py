def solution():
    # Let x be the middle brother's age
    # Then the youngest brother's age is x-1, and the oldest brother's age is x+1
    # Their ages add up to 96, so we can write an equation: (x-1) + x + (x+1) = 96
    # Simplifying the equation, we get: 3x = 96 --> x = 32
    # Therefore, the youngest brother is x-1 = 31 years old
    result = 31
    return result

print(solution())