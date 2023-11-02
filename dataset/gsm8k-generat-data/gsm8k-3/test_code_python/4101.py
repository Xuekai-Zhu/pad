def solution():
    """Buffy has a sailboat with a planing hull that she sails in the Gulf of Mexico.  Under optimal wind conditions, the use of two sails brings the ship to the speed of 50 knots, whereas under the same conditions, the use of one sail brings her ship to the speed of 25 knots.  A knot is a nautical term for speed equal to 1 nautical mile per hour, and one nautical mile equals 1.15 land miles.  If she travels in her sailboat under optimal wind conditions for 4 hours with one sail and then for another 4 hours with two sails, what is the total distance, in land miles, that she will travel?"""
    # Define the speeds of the sailboat with one and two sails
    ONE_SAIL_SPEED = 25  # in knots
    TWO_SAILS_SPEED = 50  # in knots

    # Define the time sailed with one sail and two sails
    ONE_SAIL_TIME = 4  # in hours
    TWO_SAILS_TIME = 4  # in hours

    # Convert the speeds from knots to land miles per hour
    ONE_SAIL_LMPH = ONE_SAIL_SPEED * 1.15
    TWO_SAILS_LMPH = TWO_SAILS_SPEED * 1.15

    # Calculate the distances traveled with one sail and two sails
    ONE_SAIL_DIST = ONE_SAIL_LMPH * ONE_SAIL_TIME
    TWO_SAILS_DIST = TWO_SAILS_LMPH * TWO_SAILS_TIME

    # Calculate the total distance traveled
    total_distance = ONE_SAIL_DIST + TWO_SAILS_DIST

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())