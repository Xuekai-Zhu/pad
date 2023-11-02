def solution():
    """Tom paints a room that has 5 walls. Each wall is 2 meters by 3 meters. John can paint 1 square meter every 10 minutes. He has 10 hours to paint everything. How many hours does he have to spare?"""
    num_walls = 5
    wall_width = 2
    wall_height = 3
    wall_area = wall_width * wall_height
    total_area = num_walls * wall_area
    painting_speed = 1/10  # square meters per minute
    painting_time = total_area / painting_speed
    total_time = painting_time / 60  # hours
    time_left = 10 - total_time
    result = time_left
    return result

print(solution())