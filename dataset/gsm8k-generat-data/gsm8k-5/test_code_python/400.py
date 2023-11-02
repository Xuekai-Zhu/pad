def solution():
    water_weight = 20  # Karen packs 20 pounds of water
    food_weight = 10  # Karen packs 10 pounds of food
    gear_weight = 20  # Karen packs 20 pounds of gear
    total_weight = water_weight + food_weight + gear_weight  # Calculate the initial weight of her backpack

    water_consumed = 2 * 6  # Karen drinks 2 pounds of water per hour for 6 hours
    food_consumed = (1/3) * water_consumed  # Karen eats 1/3rd the weight of food per hour as water per hour for 6 hours

    # Calculate the remaining weight of her backpack after 6 hours
    remaining_weight = total_weight - water_consumed - food_consumed
    result = remaining_weight
    return result

print(solution())