def solution():
    total_shares = 40
    ratio = 3  # Joshua's share is three times Justin's share

    # Calculate Justin's share
    justin_share = total_shares / (ratio + 1)

    # Calculate Joshua's share
    joshua_share = justin_share * ratio
    result = joshua_share
    return result

print(solution())