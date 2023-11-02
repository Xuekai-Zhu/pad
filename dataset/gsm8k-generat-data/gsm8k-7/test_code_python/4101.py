def solution():
    speed_1_sail = 25  # in knots
    speed_2_sails = 50  # in knots
    time_1_sail = 4  # in hours
    time_2_sails = 4  # in hours
    knot_to_mile = 1.15

    # Calculate the distance traveled with 1 sail
    dist_1_sail = speed_1_sail * time_1_sail

    # Calculate the distance traveled with 2 sails
    dist_2_sails = speed_2_sails * time_2_sails

    # Calculate the total distance traveled in nautical miles
    total_dist_nautical = dist_1_sail + dist_2_sails

    # Convert nautical miles to land miles
    total_dist_land = total_dist_nautical * knot_to_mile

    result = total_dist_land
    return result

print(solution())