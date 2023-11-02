def solution():
    # Define the distance of the detour, which is 20% longer than the original 30 miles
    detour_distance = 30 * 1.2

    # Calculate the total distance of the round trip
    total_distance = 30 + detour_distance

    # Calculate the total time Kim spent driving
    driving_time = total_distance / 44 * 60

    # Add the 30 minutes she spent at her friend's house
    total_time = driving_time + 30

    result = total_time
    return result

print(solution())