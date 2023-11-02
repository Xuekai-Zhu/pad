def solution():
    """Lindsay is doing the laundry, and thinks she has missed some socks. There are 50 socks that need washing. If she washes 10 pairs of socks and 15 loose socks, how many socks has Lindsay missed?"""
    socks_washed = (10 * 2) + 15
    total_socks = 50
    socks_missed = total_socks - socks_washed
    result = socks_missed
    return result

print(solution())