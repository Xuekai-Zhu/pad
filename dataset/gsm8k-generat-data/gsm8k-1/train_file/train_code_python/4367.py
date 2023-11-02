def solution():
    """Joy has 250 feet of tape. She wants to wrap the tape around a field that is 20 feet wide and 60 feet long. How much tape will Joy have left over after wrapping tape around the field once?"""
    tape_length = 250
    field_width = 20
    field_length = 60
    perimeter = 2 * (field_width + field_length)
    tape_used = perimeter
    tape_leftover = tape_length - tape_used
    result = tape_leftover
    return result

print(solution())