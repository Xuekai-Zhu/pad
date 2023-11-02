def solution():
    total_mushrooms = 30
    gilled_ratio = 1/10  # 1 gilled mushroom for every 9 spotted mushrooms
    spotted_ratio = 9/10  # 9 spotted mushrooms for every 1 gilled mushroom

    # Calculate the number of spotted mushrooms
    num_spotted_mushrooms = total_mushrooms * spotted_ratio

    # Calculate the number of gilled mushrooms
    num_gilled_mushrooms = total_mushrooms * gilled_ratio

    result = num_gilled_mushrooms
    return result

print(solution())