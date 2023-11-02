def solution():
    
    ella_food_per_day = 20
    dog_food_per_day = 4 * ella_food_per_day
    total_food_per_day = ella_food_per_day + dog_food_per_day
    total_food_10_days = total_food_per_day * 10
    result = total_food_10_days
    return result

print(solution())