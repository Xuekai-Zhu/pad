def solution():
    ella_daily_food = 20 # Ella eats 20 pounds of food per day
    dog_daily_food = ella_daily_food * 4 # Dog eats 4 pounds of food for every 1 pound Ella eats
    total_food_per_day = ella_daily_food + dog_daily_food # Total food consumed per day
    total_food_in_10_days = 10 * total_food_per_day # Total food consumed in 10 days
    result = total_food_in_10_days
    return result

print(solution())