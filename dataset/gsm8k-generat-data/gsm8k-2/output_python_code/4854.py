def solution():
    """Danny helps his friends carpool to work. He has to drive 8 miles to the first friend's house, half that distance to the second friend's house, then 3 times the total distance driven so far to get to work. How many miles does Danny drive between the second friend's house and work?"""
    first_friend_distance = 8
    second_friend_distance = first_friend_distance / 2
    total_distance = first_friend_distance + second_friend_distance
    distance_to_work = 3 * total_distance - first_friend_distance - second_friend_distance
    result = distance_to_work
    return result

print(solution())