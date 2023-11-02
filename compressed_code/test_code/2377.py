def solution():
    
    empty_bowl_weight = 420
    food_per_day = 60
    days_between_refills = 3
    food_per_refill = food_per_day * days_between_refills
    total_food_eaten = food_per_refill - 14
    new_bowl_weight = empty_bowl_weight + total_food_eaten
    result = new_bowl_weight
    return result

print(solution())