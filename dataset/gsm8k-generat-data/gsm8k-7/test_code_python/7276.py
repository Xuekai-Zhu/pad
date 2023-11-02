def solution():
    # Let a be the number of apples, p be the number of pears, and b be the number of bananas
    # We know that p = a + 2 and b = p + 3
    # We also know that a + p + b = 19
    # Substitute p and b in the third equation with the first two equations
    a = (19 - 5) / 3
    b = a + 5

    result = b
    return result

print(solution())