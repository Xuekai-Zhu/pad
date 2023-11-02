def solution():
    
    num_walls = 5
    wall_width = 2
    wall_height = 3
    wall_area = wall_width * wall_height
    total_area = num_walls * wall_area
    painting_speed = 1/10  
    painting_time = total_area / painting_speed
    total_time = painting_time / 60  
    time_left = 10 - total_time
    result = time_left
    return result

print(solution())