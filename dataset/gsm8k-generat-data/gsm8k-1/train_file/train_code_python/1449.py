def solution():
    """Caroline has 40 pairs of socks. She loses 4 pairs of socks at the laundromat. Of the remaining pairs of socks, she donates two-thirds to the thrift store. Then she purchases 10 new pairs of socks, and she receives 3 new pairs of socks as a gift from her dad. How many pairs of socks does Caroline have in total?"""
    initial_socks = 40
    lost_socks = 4
    remaining_socks = initial_socks - lost_socks
    donated_socks = remaining_socks * (2/3)
    remaining_socks -= donated_socks
    purchased_socks = 10
    gifted_socks = 3
    total_socks = remaining_socks + purchased_socks + gifted_socks
    result = total_socks
    return result

print(solution())