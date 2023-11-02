def solution():
    """The distance between Arizona and New York is around 2,000 miles by plane. The distance between the 2 different US states increases by 40% if someone decides to drive instead of flying. Missouri is midway between Arizona and New York. How far away is Missouri from New York if someone decides to go by car?"""
    plane_distance = 2000
    car_distance = plane_distance * 1.4
    missouri_distance = plane_distance / 2
    distance_to_new_york = car_distance - missouri_distance
    result = distance_to_new_york
    return result

print(solution())