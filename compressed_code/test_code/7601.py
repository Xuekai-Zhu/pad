def solution():
    
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