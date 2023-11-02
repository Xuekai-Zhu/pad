def solution():
    """Steve has 25 socks. He has 4 pairs of socks that match, and all the others don't match. How many mismatching socks does Steve have altogether?"""
    matching_socks = 4 * 2  # 4 pairs of matching socks
    mismatching_socks = 25 - matching_socks
    result = mismatching_socks
    return result

print(solution())