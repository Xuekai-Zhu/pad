def solution():
    
    land_area = 200 * 900  
    rabbit_graze_area = 10 * 9  
    no_of_rabbits = 100
    daily_graze_area = no_of_rabbits * rabbit_graze_area  
    days_to_clear_all_grass = land_area // daily_graze_area
    result = days_to_clear_all_grass
    return result

print(solution())