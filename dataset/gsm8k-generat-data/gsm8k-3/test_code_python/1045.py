def solution():
    """Andy has 4 times as many white socks as he has black socks. If he loses half his white socks, how many more white socks does he still have than black socks if he has 6 black socks?"""
    # Define the ratio of white socks to black socks
    WHITE_TO_BLACK_RATIO = 4

    # Define the number of black socks
    black_socks = 6

    # Calculate the number of white socks
    white_socks = WHITE_TO_BLACK_RATIO * black_socks

    # Calculate the number of white socks remaining after losing half
    white_socks_remaining = white_socks // 2

    # Calculate the difference between the number of white socks remaining and the number of black socks
    difference = white_socks_remaining - black_socks

    # Display the difference
    result = difference
    return result

print(solution())