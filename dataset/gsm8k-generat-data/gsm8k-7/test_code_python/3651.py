def solution():
    num_matching_pairs = 4
    num_socks = 25

    # Calculate the total number of matching socks
    total_matching_socks = num_matching_pairs * 2

    # Calculate the total number of mismatching socks
    total_mismatching_socks = num_socks - total_matching_socks
    result = total_mismatching_socks
    return result

print(solution())