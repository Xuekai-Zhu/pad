def solution():
    # Convert 50 knots and 25 knots to land miles per hour
    speed_2_sails = 50 * 1.15
    speed_1_sail = 25 * 1.15

    # Calculate the distance traveled in the first 4 hours with one sail
    distance_1_sail = speed_1_sail * 4

    # Calculate the distance traveled in the next 4 hours with two sails
    distance_2_sails = speed_2_sails * 4

    # Calculate the total distance traveled
    total_distance = distance_1_sail + distance_2_sails
    result = total_distance
    return result

print(solution())