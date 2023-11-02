def solution():
    """Tony has to run several errands in a day. He needs to drive 10 miles to get groceries, 15 miles to get a haircut, and 5 miles to go to a doctor's appointment. How many miles will Tony have driven when he is halfway through driving around for his errands?"""
    # Calculate the total distance Tony needs to drive
    total_distance = 10 + 15 + 5

    # Calculate half of the total distance
    half_distance = total_distance / 2

    # Initialize a variable to track the distance driven so far
    distance_driven = 0

    # Determine which errand Tony is on when he reaches halfway point and add the distance to the distance driven so far
    if half_distance <= 10:
        distance_driven += half_distance
    elif half_distance <= 25:
        distance_driven += 10 + (half_distance - 10) * 2 / 3
    else:
        distance_driven += 10 + 10 * 2 / 3 + (half_distance - 25)

    # Return the result
    result = distance_driven
    return result

print(solution())