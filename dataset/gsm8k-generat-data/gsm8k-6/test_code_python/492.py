def solution():
    # Calculate the number of judges in each age category
    under_30 = 0.1 * 40
    from_30_to_50 = 0.6 * 40
    over_50 = 40 - under_30 - from_30_to_50  # the remaining judges are over 50

    result = over_50
    return result

print(solution())