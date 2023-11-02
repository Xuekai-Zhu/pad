def solution():
    # Define the total number of socks and the fraction that are white
    total_socks = 180
    white_fraction = 2/3

    # Calculate the number of white socks and the number of blue socks
    white_socks = white_fraction * total_socks
    blue_socks = total_socks - white_socks

    result = blue_socks
    return result

print(solution())