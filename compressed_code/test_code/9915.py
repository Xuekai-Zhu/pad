def solution():
    
    hours_walked = 3
    km_per_hour = 5
    total_km_needed = 30
    
    km_walked = hours_walked * km_per_hour
    km_left_to_walk = total_km_needed - km_walked
    hours_needed = km_left_to_walk / km_per_hour
    
    return hours_needed

print(solution())