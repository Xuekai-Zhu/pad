def solution():
    # Calculate the total height of the first 10 floors
    first_half_height = 10 * 12

    # Calculate the total height of the second half of the building
    second_half_height = 0
    for floor in range(11, 21):
        height = 12 + (floor - 11) * 3
        second_half_height += height

    # Calculate the total height of the building
    total_height = first_half_height + second_half_height
    result = total_height
    return result

print(solution())