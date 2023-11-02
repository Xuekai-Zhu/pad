def solution():
    
    matching_pairs = 4
    socks_in_pair = 2
    total_matching_socks = matching_pairs * socks_in_pair
    total_socks = 25
    mismatching_socks = total_socks - total_matching_socks
    result = mismatching_socks
    return result

print(solution())