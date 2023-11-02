def solution():
    # Let x be the number of damaged books
    # Then, 6x-8 is the number of obsolete books
    # The total number of books removed is 69
    # So we can set up the equation:
    x + (6x - 8) = 69

    # Simplify and solve for x
    7x - 8 = 69
    7x = 77
    x = 11

    # Therefore, there were 11 damaged books
    result = x
    return result

print(solution())