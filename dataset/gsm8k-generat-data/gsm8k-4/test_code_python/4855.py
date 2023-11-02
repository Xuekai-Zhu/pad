def solution():
    """Danny helps his friends carpool to work. He has to drive 8 miles to the first friend's house, half that distance to the second friend's house, then 3 times the total distance driven so far to get to work. How many miles does Danny drive between the second friend's house and work?"""
    # Define the distance to the first friend's house
    distance_1 = 8

    # Calculate the distance to the second friend's house
    distance_2 = distance_1 / 2

    # Calculate the total distance driven so far
    total_distance = distance_1 + distance_2

    # Calculate the distance from the second friend's house to work
    distance_3 = 3 * total_distance - distance_1 - distance_2

    # return the result
    result = distance_3
    return result

print(solution())