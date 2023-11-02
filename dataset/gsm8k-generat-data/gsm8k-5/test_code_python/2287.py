def solution():
    # Let x be the number of purple cars
    # Then the number of red cars is x + 6
    # And the number of green cars is 4(x + 6) = 4x + 24
    # The total number of cars is x + (x + 6) + (4x + 24) = 6x + 30

    # We know that the total number of cars is 312
    # So 6x + 30 = 312
    # Solving for x, we get x = 47

    # Therefore, the number of purple cars is 47
    result = 47
    return result

print(solution())