def solution():
    # Calculate the perimeter of the field
    perimeter = 2 * (20 + 60)

    # Calculate the amount of tape used for one loop around the field
    tape_used = perimeter

    # Calculate the amount of tape left over after one loop around the field
    tape_left_over = 250 - tape_used

    result = tape_left_over
    return result

print(solution())