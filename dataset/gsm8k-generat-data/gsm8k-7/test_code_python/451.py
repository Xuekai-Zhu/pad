def solution():
    num_bulbs = 40
    used_bulbs = 16

    # Calculate the number of bulbs remaining after some are used
    remaining_bulbs = num_bulbs - used_bulbs

    # Calculate the number of bulbs given to a friend
    bulbs_given = remaining_bulbs / 2

    # Calculate the number of bulbs remaining after giving some to a friend
    bulbs_remaining = remaining_bulbs - bulbs_given
    result = bulbs_remaining
    return result

print(solution())