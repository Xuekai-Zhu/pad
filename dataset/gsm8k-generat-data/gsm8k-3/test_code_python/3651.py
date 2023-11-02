def solution():
    """Steve has 25 socks. He has 4 pairs of socks that match, and all the others don't match. How many mismatching socks does Steve have altogether?"""
    # Define the number of matching pairs of socks
    matching_pairs = 4

    # Calculate the total number of matching socks
    matching_socks = matching_pairs * 2

    # Calculate the number of mismatching socks
    mismatching_socks = 25 - matching_socks

    # Display the number of mismatching socks
    result = mismatching_socks
    return result

print(solution())