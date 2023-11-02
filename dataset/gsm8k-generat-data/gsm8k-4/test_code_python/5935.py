def solution():
    """Kim drives 30 miles to her friend's house.  On the way back she has to take a detour that is 20% longer.  
    She spends 30 minutes at her friend's house.  She drives at a speed of 44 mph.  How long did she spend away from home?"""
    # Define the distance to Kim's friend's house
    distance = 30

    # Calculate the length of the detour
    detour_length = distance * 0.2

    # Calculate the total distance of the trip
    total_distance = distance + detour_length

    # Calculate the total time spent driving
    driving_time = total_distance / 44

    # Add the 30 minutes spent at her friend's house
    total_time = driving_time + 0.5

    # Return the result in hours and round to two decimal places
    result = round(total_time, 2)
    return result

print(solution())