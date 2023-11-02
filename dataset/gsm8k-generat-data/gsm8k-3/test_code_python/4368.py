def solution():
    """Joy has 250 feet of tape. She wants to wrap the tape around a field that is 20 feet wide and 60 feet long. How much tape will Joy have left over after wrapping tape around the field once?"""
    # Calculate the perimeter of the field
    perimeter = 2 * (20 + 60)

    # Calculate the amount of tape used to wrap around the field once
    tape_used = perimeter

    # Calculate the amount of tape left over
    tape_left = 250 - tape_used

    # Display the amount of tape left over
    result = tape_left
    return result

print(solution())