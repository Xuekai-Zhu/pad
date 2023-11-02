def solution():
    distance_to_friend = 30
    detour_percent = 0.2  # 20% longer
    time_at_friend's_house = 30 / 60  # convert to hours
    speed = 44  # mph

    # Calculate the distance of the detour
    detour_distance = distance_to_friend * detour_percent

    # Calculate the total distance of the entire trip
    total_distance = distance_to_friend + detour_distance

    # Calculate the total time spent driving
    total_time_driving = total_distance / speed

    # Calculate the total time away from home
    total_time = total_time_driving + time_at_friend's_house
    result = total_time
    return result

print(solution())