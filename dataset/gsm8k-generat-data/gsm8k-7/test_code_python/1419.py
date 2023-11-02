def solution():
    total_distance = 20
    first_day_distance = 2
    num_days = 5
    
    # Calculate the total additional distance he needs to cover in the remaining 4 days
    remaining_distance = total_distance - first_day_distance
    
    # Calculate the additional distance he needs to cover each day
    additional_distance_per_day = remaining_distance / 4
    
    # Calculate the distance he ran on the 5th day
    distance_on_fifth_day = first_day_distance + (additional_distance_per_day * 4)
    result = distance_on_fifth_day
    return result

print(solution())