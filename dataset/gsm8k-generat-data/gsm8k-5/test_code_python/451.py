def solution():
    total_bulbs = 40  # John buys a box of 40 light bulbs
    used_bulbs = 16  # John uses 16 light bulbs
    bulbs_left = total_bulbs - used_bulbs  # John has this many light bulbs left

    # John gives half of the bulbs left to a friend
    bulbs_given = bulbs_left / 2
    bulbs_remaining = bulbs_left - bulbs_given

    result = bulbs_remaining
    return result

print(solution())