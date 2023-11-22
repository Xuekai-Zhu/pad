def solution():
    
    # Let x be the number of tennis balls in the second set
    # Then, the number of tennis balls in the first set is x + 4
    # And the number of tennis balls in the third set is 2x / 2
    # We know that the total number of tennis balls retrieved is 19
    # So, we can write the equation:
    # x + (x + 4) + (x / 2) = 19
    # Solving for x, we get:
    x = 19 - 4

    # Display the number of tennis balls in the first set
    result = x
    return result

print(solution())