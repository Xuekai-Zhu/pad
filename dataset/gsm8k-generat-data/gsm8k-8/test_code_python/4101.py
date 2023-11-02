def solution():
    # Convert knot speed to land speed
    one_sail_speed = 25 * 1.15
    two_sail_speed = 50 * 1.15

    # Calculate the distance traveled with one sail for 4 hours
    distance_one_sail = one_sail_speed * 4

    # Calculate the distance traveled with two sails for 4 hours
    distance_two_sails = two_sail_speed * 4

    # Calculate the total distance
    total_distance = distance_one_sail + distance_two_sails
    result = total_distance
    return result

print(solution())