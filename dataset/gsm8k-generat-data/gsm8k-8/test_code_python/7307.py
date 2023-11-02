def solution():
    puppy_cost = 10
    food_per_day = 1/3
    food_per_week = food_per_day * 7
    food_for_3_weeks = food_per_week * 3
    num_food_bags = food_for_3_weeks / 3.5
    total_food_cost = num_food_bags * 2
    total_cost = puppy_cost + total_food_cost
    result = total_cost
    return result

print(solution())