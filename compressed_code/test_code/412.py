def solution():
    
    mom_food_per_day = 1.5 * 3
    puppies_food_per_day = 0.5 * 2 * 5
    total_food_per_day = mom_food_per_day + puppies_food_per_day
    total_food_for_6_days = total_food_per_day * 6
    result = total_food_for_6_days
    return result

print(solution())