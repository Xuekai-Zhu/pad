def solution():
    distance_to_friend1 = 8
    distance_to_friend2 = distance_to_friend1 / 2
    total_distance_to_work = distance_to_friend1 + distance_to_friend2

    distance_to_second_friend = distance_to_friend2 - distance_to_friend1

    distance_from_second_friend_to_work = 3 * (total_distance_to_work)

    distance_driven_between_second_friend_and_work = distance_from_second_friend_to_work - total_distance_to_work
    result = distance_driven_between_second_friend_and_work
    return result

print(solution())