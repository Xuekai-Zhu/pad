def solution():
    total_distance = 150
    days_riding = 12
    distance_per_day = 12
    
    # Calculate the total distance already ridden
    total_ridden = days_riding * distance_per_day
    
    # Calculate the remaining distance to complete the goal
    remaining_distance = total_distance - total_ridden
    
    # Calculate the distance to ride on the 13th day
    distance_on_13th_day = remaining_distance
    
    result = distance_on_13th_day
    return result

print(solution())