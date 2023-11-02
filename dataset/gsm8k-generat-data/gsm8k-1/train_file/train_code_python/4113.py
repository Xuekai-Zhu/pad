def solution():
    """Kristin can run three times faster than Sarith. If Kristin runs 12 times around the adult football field and Sarith runs at the same time around the children's football field that is half the distance as the other field, how many laps did Sarith go around the children's football field?"""
    kristin_laps = 12
    sarith_speed_ratio = 1/3
    sarith_laps = kristin_laps / sarith_speed_ratio
    sarith_distance_ratio = 1/2
    sarith_laps_around_childrens_field = sarith_laps * (sarith_distance_ratio ** 2)
    result = sarith_laps_around_childrens_field
    return result

print(solution())