def solution():
    # Distance to first friend's house
    distance_first_friend = 8

    # Distance to second friend's house
    distance_second_friend = distance_first_friend / 2

    # Total distance driven so far
    total_distance = distance_first_friend + distance_second_friend

    # Distance from second friend's house to work
    distance_to_work = 3 * total_distance - distance_first_friend - distance_second_friend
    result = distance_to_work
    return result

print(solution())