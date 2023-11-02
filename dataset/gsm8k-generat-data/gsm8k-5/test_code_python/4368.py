def solution():
    # Calculate the total length of tape needed to wrap around the field once
    perimeter = 2 * (20 + 60)  # Perimeter of a rectangle is twice the sum of its sides
    tape_needed = perimeter

    # Calculate how much tape Joy will have left over
    tape_leftover = 250 - tape_needed
    result = tape_leftover
    return result

print(solution())