def solution():
    # Calculate the space taken up by the big toenails
    space_taken_by_big_toenails = 2 * 20

    # Calculate the space taken up by the regular toenails
    space_taken_by_regular_toenails = 40

    # Calculate the remaining space in the jar
    remaining_space = 100 - space_taken_by_big_toenails - space_taken_by_regular_toenails

    # Calculate the number of regular toenails that can fit in the remaining space
    regular_toenails_in_remaining_space = remaining_space / 1

    result = regular_toenails_in_remaining_space
    return result

print(solution())