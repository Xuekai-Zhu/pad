def solution():
    """Buffy has a sailboat with a planing hull that she sails in the Gulf of Mexico. Under optimal wind conditions, the use of two sails brings the ship to the speed of 50 knots, whereas under the same conditions, the use of one sail brings her ship to the speed of 25 knots. A knot is a nautical term for speed equal to 1 nautical mile per hour, and one nautical mile equals 1.15 land miles. If she travels in her sailboat under optimal wind conditions for 4 hours with one sail and then for another 4 hours with two sails, what is the total distance, in land miles, that she will travel?"""
    
    # Calculate the distance with one sail for 4 hours
    distance_one_sail = 25 * 4 * 1.15

    # Calculate the distance with two sails for 4 hours
    distance_two_sails = 50 * 4 * 1.15

    # Calculate the total distance traveled
    total_distance = distance_one_sail + distance_two_sails

    # Return the result
    result = total_distance
    return result

print(solution())