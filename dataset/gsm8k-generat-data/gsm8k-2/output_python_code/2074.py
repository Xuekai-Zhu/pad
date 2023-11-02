def solution():
    """A father and a son start approaching each other at the same time from opposite ends of a hallway that is 16m long. If the father is walking three times as fast as the son, at what distance from the father's end of the hallway will they meet?"""
    hallway_length = 16
    father_speed = 3
    son_speed = 1
    ratio = father_speed / (father_speed + son_speed)
    distance_from_father_end = ratio * hallway_length
    result = distance_from_father_end
    return result

print(solution())