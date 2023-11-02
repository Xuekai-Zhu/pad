def solution():
    matching_pairs = 4  # Steve has 4 pairs of matching socks
    total_socks = 25  # Steve has 25 socks in total

    # Calculate the number of mismatching socks Steve has
    mismatching_socks = total_socks - (matching_pairs * 2)

    result = mismatching_socks
    return result

print(solution())