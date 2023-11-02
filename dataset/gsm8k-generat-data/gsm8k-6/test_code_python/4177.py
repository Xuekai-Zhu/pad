def solution():
    # Set up the equations
    # Let x be the weight of the chihuahua
    # Then the weight of the pitbull is 3x, and the weight of the great dane is 10 + 3(3x) = 9x + 10
    # The total weight is x + 3x + 9x + 10 = 13x + 10
    # We are given that the total weight is 439 pounds, so 13x + 10 = 439
    # Solving for x, we get x = 33.769, and then the weight of the great dane is 9x + 10 = 306.921 pounds
    great_dane_weight = 9*33.769 + 10
    result = great_dane_weight
    return result

print(solution())