def solution():
    """Trish likes to go for walks every day. One day, she goes on a 1-mile walk. Every subsequent day, she doubles the distance she walked the previous day. On what day does she walk more than 10 times further than she did on the first day?"""
    first_day_distance = 1
    current_distance = first_day_distance
    target_distance = 10 * first_day_distance
    
    # Keep doubling distance until it is greater than target distance
    day = 1
    while current_distance < target_distance:
        current_distance *= 2
        day += 1
    
    result = day
    return result

print(solution())