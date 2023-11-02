def solution():
    
    largest_rate = 3
    medium_rate = largest_rate / 2
    smallest_rate = medium_rate / 3
    total_rate = largest_rate + medium_rate + smallest_rate
    time_in_minutes = 2 * 60
    total_water_leaked = total_rate * time_in_minutes
    result = total_water_leaked
    return result

print(solution())