def solution():
    
    mom_food_per_day = 1.5 * 3
    puppy_food_per_day = 0.5 * 2 * 5
    total_food_per_day = mom_food_per_day + puppy_food_per_day
    total_food_for_six_days = total_food_per_day * 6
    result = total_food_for_six_days
    return result

print(solution())