def solution():
    speed_one_sail = 25  # Buffy's speed with one sail is 25 knots
    speed_two_sails = 50  # Buffy's speed with two sails is 50 knots
    time_one_sail = 4  # Buffy sails with one sail for 4 hours
    time_two_sails = 4  # Buffy sails with two sails for 4 hours
    knot_to_land_mile = 1.15  # One knot equals 1.15 land miles

    # Calculate the distance traveled with one sail
    distance_one_sail = speed_one_sail * time_one_sail * knot_to_land_mile

    # Calculate the distance traveled with two sails
    distance_two_sails = speed_two_sails * time_two_sails * knot_to_land_mile

    # Calculate the total distance traveled
    total_distance = distance_one_sail + distance_two_sails
    result = total_distance
    return result

print(solution())