def solution():
    """Danny helps his friends carpool to work. He has to drive 8 miles to the first friend's house, half that distance to the second friend's house, then 3 times the total distance driven so far to get to work. How many miles does Danny drive between the second friend's house and work?"""
    # Define the distance to the first friend's house
    distance1 = 8

    # Define the distance to the second friend's house
    distance2 = distance1 / 2

    # Define the total distance driven so far
    total_distance = distance1 + distance2

    # Calculate the distance from the second friend's house to work
    distance3 = 3 * total_distance - distance1 - distance2

    # Display the distance driven by Danny between the second friend's house and work
    result = distance3
    return result

print(solution())