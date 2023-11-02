def solution():
    normal_speed = 2  # in billions of miles per hour
    black_hole_speed = 3 * normal_speed
    normal_time = 7  # in hours
    black_hole_time = 2  # in hours

    # Calculate the distance traveled at normal speed
    normal_distance = normal_speed * normal_time

    # Calculate the distance traveled at black hole speed
    black_hole_distance = black_hole_speed * black_hole_time

    # Calculate the total distance traveled
    total_distance = normal_distance + black_hole_distance
    result = total_distance
    return result

print(solution())