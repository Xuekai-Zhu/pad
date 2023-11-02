def solution():
    # Let x be the weight of the chihuahua
    x = 1

    # Calculate the weight of the pitbull
    pitbull_weight = 3 * x

    # Calculate the weight of the great dane
    great_dane_weight = 10 + 3 * pitbull_weight

    # Calculate the total weight of all three dogs
    total_weight = x + pitbull_weight + great_dane_weight

    result = great_dane_weight
    return result

print(solution())