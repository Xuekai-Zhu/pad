def solution():
    # Calculate the number of delegates with pre-printed name badges
    pre_printed = 16

    # Calculate the number of delegates without pre-printed name badges
    remaining = 36 - pre_printed

    # Calculate the number of delegates who made their own name badges
    hand_written = remaining / 2

    # Calculate the number of delegates not wearing name badges
    not_wearing = remaining - hand_written
    result = not_wearing
    return result

print(solution())