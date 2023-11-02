def solution():
    """Talia is playing football with her friends. The park they're playing at is 5 miles from Talia's house. After their game, Talia is planning to go to the grocery store 3 miles away from the park and 8 miles from her home. Starting and ending at Talia's house, how many miles does Talia drive that day?"""
    # Define the distances
    PARK_DISTANCE = 5
    STORE_DISTANCE_FROM_PARK = 3
    STORE_DISTANCE_FROM_HOME = 8

    # Calculate the total distance Talia drives
    total_distance = (PARK_DISTANCE * 2) + STORE_DISTANCE_FROM_PARK + STORE_DISTANCE_FROM_HOME

    # Display the total distance Talia drives
    result = total_distance
    return result

print(solution())