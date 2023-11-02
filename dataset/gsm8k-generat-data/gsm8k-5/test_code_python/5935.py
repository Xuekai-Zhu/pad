def solution():
    distance_to_friend = 30  # Kim drives 30 miles to her friend's house
    detour_percentage = 20  # Kim has to take a detour that is 20% longer on her way back
    detour_distance = distance_to_friend * (detour_percentage/100)  # Calculate the detour distance
    total_distance = distance_to_friend + detour_distance  # Calculate the total distance of the round trip

    # Calculate the total time for the round trip (excluding the time spent at her friend's house)
    total_time = (total_distance / 44) * 60

    # Add the time spent at her friend's house
    total_time += 30

    result = total_time
    return result

print(solution())