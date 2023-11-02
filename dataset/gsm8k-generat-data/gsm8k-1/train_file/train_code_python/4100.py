def solution():
    """Buffy has a sailboat with a planing hull that she sails in the Gulf of Mexico. Under optimal wind conditions, the use of two sails brings the ship to the speed of 50 knots, whereas under the same conditions, the use of one sail brings her ship to the speed of 25 knots. A knot is a nautical term for speed equal to 1 nautical mile per hour, and one nautical mile equals 1.15 land miles. If she travels in her sailboat under optimal wind conditions for 4 hours with one sail and then for another 4 hours with two sails, what is the total distance, in land miles, that she will travel?"""
    one_sail_speed = 25 # knots
    two_sail_speed = 50 # knots
    time_on_one_sail = 4 # hours
    time_on_two_sails = 4 # hours
    nautical_miles_per_hour = 1 # knot
    land_miles_per_nautical_mile = 1.15 # miles
    distance_with_one_sail = one_sail_speed * time_on_one_sail
    distance_with_two_sails = two_sail_speed * time_on_two_sails
    total_distance_in_nautical_miles = distance_with_one_sail + distance_with_two_sails
    total_distance_in_land_miles = total_distance_in_nautical_miles * nautical_miles_per_hour * land_miles_per_nautical_mile
    result = total_distance_in_land_miles
    return result

print(solution())