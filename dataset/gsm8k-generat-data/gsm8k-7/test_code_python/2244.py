def solution():
    total_chickens = 75

    # Let x be the number of roosters
    # Then the number of hens is 9x - 5
    # And the total number of chickens is x + (9x - 5) = 10x - 5
    # So we can set 10x - 5 = total_chickens and solve for x

    x = (total_chickens + 5) / 10
    num_hens = 9*x - 5
    result = num_hens
    return result

print(solution())