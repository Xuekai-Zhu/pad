def solution():
    """Joan has 180 socks. Two thirds of the socks are white, and the rest of the socks are blue. How many blue socks does Joan have?"""
    total_socks = 180
    white_socks = (2/3) * total_socks
    blue_socks = total_socks - white_socks
    result = blue_socks
    return result

print(solution())