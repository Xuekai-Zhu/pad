def solution():
    
    total_distance = 20
    first_day_distance = 2
    days_of_running = 5
    total_distance -= first_day_distance
    for i in range(2, days_of_running + 1):
        total_distance -= (first_day_distance + (i - 1))

    fifth_day_distance = first_day_distance + (days_of_running - 1)
    result = fifth_day_distance
    return result

print(solution())