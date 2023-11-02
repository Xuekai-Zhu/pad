def solution():
    appearance_time_mars = 1210
    appearance_time_jupiter = 2141
    appearance_time_uranus = 3116
    time_mars_to_jupiter = appearance_time_jupiter - appearance_time_mars
    time_jupiter_to_uranus = appearance_time_uranus - appearance_time_jupiter
    total_time = time_mars_to_jupiter + time_jupiter_to_uranus
    result = total_time
    
    return result

print(solution())