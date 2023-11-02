def solution():
    # Calculate the distance thrown on Saturday
    distance_sat = 20

    # Calculate the distance thrown on Sunday
    distance_sun = 2 * 20

    # Calculate the total distance thrown on Saturday
    total_distance_sat = 20 * distance_sat

    # Calculate the total distance thrown on Sunday
    total_distance_sun = 30 * distance_sun

    # Calculate the total distance thrown in the two days
    total_distance = total_distance_sat + total_distance_sun
    result = total_distance
    return result

print(solution())