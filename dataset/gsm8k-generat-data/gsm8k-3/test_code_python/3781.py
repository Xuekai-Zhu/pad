def solution():
    """Joan has 180 socks. Two thirds of the socks are white, and the rest of the socks are blue. How many blue socks does Joan have?"""
    # Define the total number of socks and the proportion of white socks
    total_socks = 180
    white_proportion = 2/3

    # Calculate the number of white socks
    white_socks = white_proportion * total_socks

    # Calculate the number of blue socks
    blue_socks = total_socks - white_socks

    # Display the number of blue socks
    result = blue_socks
    return result

print(solution())