def solution():
    num_walls = 5
    wall_width = 2
    wall_height = 3
    wall_area = wall_width * wall_height
    total_area = num_walls * wall_area
    time_per_square_meter = 10  # minutes
    total_time = 10 * 60 * 10  # 10 hours in minutes
    time_to_paint = total_area * time_per_square_meter
    time_left = (total_time - time_to_paint) / 60  # convert to hours
    result = time_left
    return result

print(solution())