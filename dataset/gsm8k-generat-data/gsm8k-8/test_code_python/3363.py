def solution():
    # Define the number of pairs of black socks
    black_pairs = x

    # Define the number of pairs of blue socks
    blue_pairs = x + 3

    # Define the number of pairs of white socks
    white_pairs = x + 1

    # Define the number of pairs of red socks
    red_pairs = 6 / 2  # Since Joseph has twice as many blue socks as red socks

    # Calculate the total number of socks
    total_socks = (black_pairs * 2) + (blue_pairs * 2) + (white_pairs * 2) + (red_pairs * 2)

    result = total_socks
    return result

print(solution())