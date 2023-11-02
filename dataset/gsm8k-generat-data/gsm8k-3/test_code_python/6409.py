def solution():
    """James has 20 pairs of red socks and half as many black socks.  He has twice as many white socks as red and black combined.  How many total socks does he have combined?"""
    # Define the number of red socks and black socks
    red_socks = 20 * 2
    black_socks = red_socks / 2

    # Define the number of white socks
    white_socks = (red_socks + black_socks) * 2

    # Calculate the total number of socks
    total_socks = (red_socks + black_socks + white_socks) * 2

    # Display the total number of socks
    result = total_socks
    return result

print(solution())