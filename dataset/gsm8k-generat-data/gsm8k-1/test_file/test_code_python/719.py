def solution():
    """The restaurant has 170 normal chairs and 23 chairs for babies. If 20 of the normal chairs and 13 of the baby chairs were sent to the carpenter for repair, how many chairs does the restaurant have left?"""
    normal_chairs = 170
    baby_chairs = 23
    normal_chairs_repaired = 20
    baby_chairs_repaired = 13
    total_chairs = normal_chairs + baby_chairs
    total_chairs_repaired = normal_chairs_repaired + baby_chairs_repaired
    chairs_left = total_chairs - total_chairs_repaired
    result = chairs_left
    return result

print(solution())