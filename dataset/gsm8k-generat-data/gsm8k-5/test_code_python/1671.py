def solution():
    river_width_start = 50  # The width of the river at the starting point
    river_width_increase = 2  # The width of the river increases by 2 yards every 10 meters
    distance_to_wider_point = 80 - river_width_start  # The distance to the wider point is the difference in widths
    distance_per_ten_meters = river_width_increase * 10  # The distance added to the width every 10 meters
    total_distance = distance_to_wider_point / distance_per_ten_meters * 10 + 50  # Total distance is the distance to wider point plus the starting point
    time = total_distance / 5  # Time is distance divided by speed
    result = time
    return result

print(solution())