def solution():
    """Kim drives 30 miles to her friend's house.  On the way back she has to take a detour that is 20% longer.  She spends 30 minutes at her friend's house.  She drives at a speed of 44 mph.  How long did she spend away from home?"""
    # Define the distance to Kim's friend's house
    distance = 30

    # Calculate the distance of the detour
    detour_distance = distance * 0.2

    # Calculate the total distance of Kim's trip
    total_distance = distance + detour_distance

    # Calculate the travel time
    travel_time = total_distance / 44

    # Add 30 minutes for the time spent at her friend's house
    total_time = travel_time + 0.5

    # Display the total time
    result = total_time
    return result

print(solution())