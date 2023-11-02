def solution():
    black_socks = 6
    white_socks = black_socks * 4
    
    # Calculate the number of white socks after losing half
    white_socks_left = white_socks / 2
    
    # Calculate the difference between white and black socks
    difference = white_socks_left - black_socks
    
    result = difference
    return result

print(solution())