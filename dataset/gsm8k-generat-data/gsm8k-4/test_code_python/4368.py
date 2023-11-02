def solution():
    """Joy has 250 feet of tape. She wants to wrap the tape around a field that is 20 feet wide and 60 feet long. How much tape will Joy have left over after wrapping tape around the field once?"""
    # Define the dimensions of the field
    field_width = 20
    field_length = 60

    # Calculate the perimeter of the field
    field_perimeter = 2 * (field_width + field_length)

    # Calculate the amount of tape used to wrap the field once
    tape_used = field_perimeter

    # Calculate the amount of tape left over
    tape_left = 250 - tape_used

    result = tape_left
    return result

print(solution())