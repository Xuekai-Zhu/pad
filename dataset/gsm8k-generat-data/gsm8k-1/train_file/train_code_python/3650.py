def solution():
    """Steve has 25 socks. He has 4 pairs of socks that match, and all the others don't match. How many mismatching socks does Steve have altogether?"""
    matching_pairs = 4
    socks_in_pair = 2
    total_matching_socks = matching_pairs * socks_in_pair
    total_socks = 25
    mismatching_socks = total_socks - total_matching_socks
    result = mismatching_socks
    return result

print(solution())