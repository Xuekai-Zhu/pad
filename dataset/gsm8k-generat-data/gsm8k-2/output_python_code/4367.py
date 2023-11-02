def solution():
    """Joy has 250 feet of tape. She wants to wrap the tape around a field that is 20 feet wide and 60 feet long. How much tape will Joy have left over after wrapping tape around the field once?"""
    field_w = 20
    field_l = 60
    perimeter = 2 * (field_l + field_w)
    tape_needed = perimeter
    tape_leftover = 250 - tape_needed
    result = tape_leftover
    return result

print(solution())