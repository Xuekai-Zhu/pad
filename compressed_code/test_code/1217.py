def solution():
    
    lake_distance = 15 * 4
    swim_speed = 1 / (20/60) 
    row_speed = swim_speed * 2
    row_time = lake_distance / row_speed 
    result = row_time
    return result

print(solution())