def solution():
    # Find the number of black socks James has
    black_socks = 20 / 2  

    # Find the number of red and black socks combined
    red_and_black_socks = 20 + black_socks  

    # Find the number of white socks James has
    white_socks = 2 * (red_and_black_socks)  

    # Find the total number of socks James has
    total_socks = red_and_black_socks + white_socks  
    result = total_socks
    return result

print(solution())