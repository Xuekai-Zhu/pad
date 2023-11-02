def solution():
    # Calculate the weight of Karen's backpack after six hours of hiking
    water_weight = 20 - 2*6  # Karen drinks 2 pounds of water per hour
    food_weight = 10 - (2/3)*2*6  # Karen eats 1/3rd the weight of water per hour
    gear_weight = 20
    total_weight = water_weight + food_weight + gear_weight
    result = total_weight
    return result

print(solution())