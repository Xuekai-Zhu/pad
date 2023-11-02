def solution():
    """Tom paints a room that has 5 walls. Each wall is 2 meters by 3 meters. John can paint 1 square meter every 10 minutes. He has 10 hours to paint everything. How many hours does he have to spare?"""
    wall_width = 2
    wall_height = 3
    walls = 5
    area_per_wall = wall_width * wall_height
    total_area = area_per_wall * walls
    time_per_square_meter = 10
    total_time = total_area * time_per_square_meter
    available_time = 10 * 60
    time_left = available_time - total_time
    hours_left = time_left / 60
    result = hours_left
    return result

print(solution())