def solution():
    """Kristin can run three times faster than Sarith. If Kristin runs 12 times around the adult football field and Sarith runs at the same time around the children's football field that is half the distance as the other field, how many laps did Sarith go around the children's football field?"""
    kristin_laps = 12
    sarith_speed_ratio = 1 / 3
    children_field_ratio = 1 / 2
    sarith_laps = kristin_laps * (children_field_ratio ** 2) / sarith_speed_ratio
    result = sarith_laps
    return result

print(solution())