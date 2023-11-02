def solution():
    
    empty_bowl_weight = 420
    daily_cat_food_amount = 60
    refill_days = 3
    total_food_amount = daily_cat_food_amount * refill_days
    remaining_food = total_food_amount - 14
    new_bowl_weight = empty_bowl_weight + remaining_food
    result = new_bowl_weight
    return result

print(solution())