def solution():
    total_sand = 95
    
    city_a_sand = 16.5
    city_b_sand = 26
    city_c_sand = 24.5
    
    # Calculate the total sand received by City D
    city_d_sand = total_sand - city_a_sand - city_b_sand - city_c_sand
    
    result = city_d_sand
    return result

print(solution())