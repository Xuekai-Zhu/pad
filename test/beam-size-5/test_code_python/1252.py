def solution():
    
    land_distance = 200
    water_speed = 10
    land_speed = 20
    water_distance = land_distance / 2
    land_time = land_distance / land_speed
    water_time = water_distance / water_speed
    total_time = land_time + water_time
    result = total_time
    return result

print(solution())