def solution():
    total_share = 40  # The total share is $40
    ratio = 3  # Joshua's share is thrice as much as Justin's
    total_ratio = 4  # The total ratio is 4 (3 + 1)

    # Calculate Justin's share
    justin_share = total_share / total_ratio * ratio

    # Calculate Joshua's share
    joshua_share = total_share - justin_share

    result = joshua_share
    return result

print(solution())