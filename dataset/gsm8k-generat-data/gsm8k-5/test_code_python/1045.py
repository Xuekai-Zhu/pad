def solution():
    black_socks = 6  # Andy has 6 black socks
    white_socks = black_socks * 4  # Andy has 4 times as many white socks as black socks
    white_socks_lost = white_socks / 2  # Andy loses half of his white socks
    white_socks_remaining = white_socks - white_socks_lost  # Andy has this many white socks remaining
    black_socks_remaining = black_socks  # Andy has the same number of black socks remaining

    # Calculate the difference between the remaining white socks and black socks
    difference = white_socks_remaining - black_socks_remaining
    result = difference
    return result

print(solution())