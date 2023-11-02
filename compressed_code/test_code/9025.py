def solution():
    
    one_sail_speed = 25 
    two_sail_speed = 50 
    time_on_one_sail = 4 
    time_on_two_sails = 4 
    nautical_miles_per_hour = 1 
    land_miles_per_nautical_mile = 1.15 
    distance_with_one_sail = one_sail_speed * time_on_one_sail
    distance_with_two_sails = two_sail_speed * time_on_two_sails
    total_distance_in_nautical_miles = distance_with_one_sail + distance_with_two_sails
    total_distance_in_land_miles = total_distance_in_nautical_miles * nautical_miles_per_hour * land_miles_per_nautical_mile
    result = total_distance_in_land_miles
    return result

print(solution())