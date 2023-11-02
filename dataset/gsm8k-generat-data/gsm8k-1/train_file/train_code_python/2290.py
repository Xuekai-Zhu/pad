def solution():
    """Trish likes to go for walks every day. One day, she goes on a 1-mile walk. Every subsequent day, she doubles the distance she walked the previous day. On what day does she walk more than 10 times further than she did on the first day?"""
    first_day = 1
    current_distance = first_day
    target_distance = 10 * first_day

    day = 1
    while True:
        if current_distance > target_distance:
            result = day
            break
        else:
            current_distance *= 2
            day += 1
    
    return result

print(solution())