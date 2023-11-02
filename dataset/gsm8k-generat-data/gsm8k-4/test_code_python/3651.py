def solution():
    """Steve has 25 socks. He has 4 pairs of socks that match, and all the others don't match. How many mismatching socks does Steve have altogether?"""
    # Define the number of matching socks
    matching_socks = 4 * 2

    # Calculate the number of mismatching socks
    mismatching_socks = 25 - matching_socks

    # Return the result
    result = mismatching_socks
    return result

print(solution())