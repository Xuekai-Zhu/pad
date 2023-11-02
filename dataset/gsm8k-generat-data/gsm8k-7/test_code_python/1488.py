def solution():
    # Let R be the number of earrings Rachel has.
    # Then Monica has 2R earrings, and Bella has 10 earrings, which is 25% of Monica's earrings.
    # Therefore, we can write:

    # 10 = 0.25 * 2R
    # 2R = 40
    # R = 20

    R = 20  # Rachel has 20 earrings
    M = 2 * R  # Monica has 40 earrings
    B = 10  # Bella has 10 earrings

    # Therefore, all of the friends have:
    total_earrings = R + M + B
    result = total_earrings
    return result

print(solution())