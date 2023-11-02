def solution():
    """Buffy has a sailboat with a planing hull that she sails in the Gulf of Mexico. Under optimal wind conditions, the use of two sails brings the ship to the speed of 50 knots, whereas under the same conditions, the use of one sail brings her ship to the speed of 25 knots. A knot is a nautical term for speed equal to 1 nautical mile per hour, and one nautical mile equals 1.15 land miles. If she travels in her sailboat under optimal wind conditions for 4 hours with one sail and then for another 4 hours with two sails, what is the total distance, in land miles, that she will travel?"""
    one_sail_speed = 25 * 1.15  # in land miles per hour
    two_sails_speed = 50 * 1.15  # in land miles per hour
    time_one_sail = 4  # in hours
    time_two_sails = 4  # in hours
    distance_one_sail = one_sail_speed * time_one_sail
    distance_two_sails = two_sails_speed * time_two_sails
    total_distance = distance_one_sail + distance_two_sails
    result = total_distance
    return result

print(solution())