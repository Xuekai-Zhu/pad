def solution():
    """The distance between Robin's house and the city center is 500 meters. He leaves the house to go to the city center. After he walks 200 meters he realizes that he forgot his bag. So he returns to his house, then goes back to the city center. How many meters does he walk in total?"""
    distance_to_center = 500
    total_distance = distance_to_center + (2 * (distance_to_center - 200))
    result = total_distance
    return result

print(solution())