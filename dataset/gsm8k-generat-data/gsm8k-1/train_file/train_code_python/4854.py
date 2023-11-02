def solution():
    """Danny helps his friends carpool to work. He has to drive 8 miles to the first friend's house, half that distance to the second friend's house, then 3 times the total distance driven so far to get to work. How many miles does Danny drive between the second friend's house and work?"""
    distance_to_first = 8
    distance_to_second = distance_to_first / 2
    total_distance = distance_to_first + distance_to_second
    distance_to_work = 3 * total_distance
    distance_between_second_and_work = distance_to_work - distance_to_first - distance_to_second
    result = distance_between_second_and_work
    return result

print(solution())