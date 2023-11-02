def solution():
    """The distance between Arizona and New York is around 2,000 miles by plane. The distance between the 2 different US states increases by 40% if someone decides to drive instead of flying. Missouri is midway between Arizona and New York. How far away is Missouri from New York if someone decides to go by car?"""
    distance_by_plane = 2000
    increase_percent = 40
    distance_by_car = distance_by_plane * (1 + (increase_percent/100))
    distance_to_missouri = distance_by_car / 2
    distance_to_new_york_from_missouri = distance_by_plane / 2
    total_distance_to_new_york = distance_to_missouri + distance_to_new_york_from_missouri
    result = total_distance_to_new_york
    return result

print(solution())