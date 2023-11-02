def solution():
    matching_socks = 4 * 2  # Steve has 4 pairs of matching socks, which is 8 matching socks altogether
    mismatching_socks = 25 - matching_socks  # Steve has 25 socks in total, so he must have 17 mismatching socks
    result = mismatching_socks
    return result

print(solution())