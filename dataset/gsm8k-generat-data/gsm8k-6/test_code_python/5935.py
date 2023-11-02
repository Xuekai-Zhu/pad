def solution():
    # Calculate the distance of the detour
    detour_distance = 30 * 1.2  # 20% longer than the original distance

    # Calculate the total distance traveled
    total_distance = 30 + detour_distance

    # Calculate the time spent driving
    driving_time = total_distance / 44

    # Calculate the total time spent away from home
    total_time = driving_time + 0.5  # 30 minutes at friend's house

    result = total_time
    return result

print(solution())