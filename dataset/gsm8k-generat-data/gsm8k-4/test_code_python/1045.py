def solution():
    """Andy has 4 times as many white socks as he has black socks. If he loses half his white socks, how many more white socks does he still have than black socks if he has 6 black socks?"""
    # Define the ratio of white socks to black socks
    white_to_black = 4

    # Calculate the total number of socks
    total_socks = white_to_black + 1

    # Calculate the number of white socks
    white_socks = total_socks / (white_to_black + 1)

    # Calculate the number of black socks
    black_socks = 6

    # Calculate the number of white socks after losing half
    white_socks_lost = white_socks / 2
    white_socks_remaining = white_socks - white_socks_lost

    # Calculate the difference between white and black socks
    difference = white_socks_remaining - black_socks

    result = difference
    return result

print(solution())