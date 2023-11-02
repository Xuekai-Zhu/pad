def solution():
    # Calculate the number of broken spiral shells
    broken_spiral_shells = 52 / 2  # half of the broken shells are spiral

    # Calculate the number of perfect spiral shells
    perfect_spiral_shells = 17 - 12  # 12 of the perfect shells are not spiral

    # Calculate the difference between the two
    difference = broken_spiral_shells - perfect_spiral_shells
    result = difference
    return result

print(solution())