def solution():
    num_red = 6  # Joseph has 6 red socks
    num_blue = 2 * num_red  # Joseph has twice as many blue socks as red socks
    num_white = num_red + 1  # Joseph has one less pair of red socks than white socks
    num_black = num_blue - 3  # Joseph has three more pairs of blue socks than black socks

    # Calculate the total number of socks
    total_socks = (num_red * 2) + (num_blue * 2) + (num_white * 2) + (num_black * 2)

    result = total_socks
    return result

print(solution())