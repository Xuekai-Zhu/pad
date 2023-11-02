def solution():
    # Calculate the total amount of food needed to feed Peter's horses for 3 days
    oats_per_horse = 4 * 2  # 4 pounds of oats, twice a day
    grain_per_horse = 3  # 3 pounds of grain, once a day
    total_food_per_horse_per_day = oats_per_horse + grain_per_horse
    total_food_per_day = total_food_per_horse_per_day * 4  # for all four horses
    total_food_for_3_days = total_food_per_day * 3
    result = total_food_for_3_days
    return result

print(solution())