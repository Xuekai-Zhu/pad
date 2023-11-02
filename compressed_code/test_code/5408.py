def solution():
    
    max_caffeine = 500
    drink_caffeine = 120
    num_drinks = 4
    total_caffeine = drink_caffeine * num_drinks
    remaining_caffeine = max_caffeine - total_caffeine
    result = remaining_caffeine
    return result

print(solution())