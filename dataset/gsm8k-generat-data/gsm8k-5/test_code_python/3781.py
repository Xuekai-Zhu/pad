def solution():
    total_socks = 180  # Joan has 180 socks
    white_socks = (2/3) * total_socks  # Two thirds of Joan's socks are white
    blue_socks = total_socks - white_socks  # The rest of Joan's socks are blue
    result = blue_socks
    return result

print(solution())