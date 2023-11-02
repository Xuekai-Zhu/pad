def solution():
    # Calculate the number of white socks Andy has
    black_socks = 6
    white_socks = black_socks * 4

    # Lose half of the white socks
    white_socks = white_socks / 2

    # Calculate the difference between white and black socks
    difference = white_socks - black_socks

    result = difference
    return result

print(solution())