def solution():
    
    total_distance = 150
    days_ridden = 12
    distance_ridden = 12 * days_ridden
    remaining_distance = total_distance - distance_ridden
    distance_on_13th_day = remaining_distance % 12
    result = distance_on_13th_day
    return result

print(solution())