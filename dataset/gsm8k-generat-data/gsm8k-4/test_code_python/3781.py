def solution():
    """Joan has 180 socks. Two thirds of the socks are white, and the rest of the socks are blue. How many blue socks does Joan have?"""
    # Define the total number of socks
    total_socks = 180

    # Calculate the number of white socks
    white_socks = total_socks * (2/3)

    # Calculate the number of blue socks
    blue_socks = total_socks - white_socks

    # return the result
    result = blue_socks
    return result

print(solution())