def solution():
    
    initial_sugar = 65
    used_today = 18
    bought_tomorrow = 50
    remaining_after_tomorrow = initial_sugar - used_today + bought_tomorrow
    result = remaining_after_tomorrow
    return result

print(solution())