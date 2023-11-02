def solution():
    # Calculate the perimeter of the field
    perimeter = 2 * (20 + 60)  # perimeter = 2(width + length)

    # Calculate the amount of tape used to wrap around the field once
    tape_used = perimeter

    # Calculate the amount of tape left over
    tape_left = 250 - tape_used

    result = tape_left
    return result

print(solution())