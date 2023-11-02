def solution():
    
    german_shepherds_per_day = 3
    bulldogs_per_day = 2
    german_shepherd_food_per_day = 5
    bulldog_food_per_day = 3
    days_per_week = 7
    total_german_shepherds = german_shepherds_per_day * days_per_week
    total_bulldogs = bulldogs_per_day * days_per_week
    total_bulldog_food = bulldogs_per_day * days_per_week
    total_food = total_german_shepherds + total_bulldog_food
    result = total_food
    return result

print(solution())