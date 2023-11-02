def solution():
    """Caroline has 40 pairs of socks. She loses 4 pairs of socks and donates two-thirds of the remaining pairs of socks to the thrift store. Then she purchases 10 new pairs of socks and receives 3 new pairs of socks as a gift from her dad. How many pairs of socks does Caroline have in total?"""
    # Define the initial number of pairs of socks
    initial_socks = 40

    # Calculate the number of socks lost at the laundromat
    lost_socks = 4

    # Calculate the number of remaining socks
    remaining_socks = initial_socks - lost_socks

    # Calculate the number of socks donated to the thrift store
    donated_socks = remaining_socks * (2/3)

    # Calculate the number of socks purchased and received as gifts
    additional_socks = 10 + 3

    # Calculate the total number of socks Caroline has
    total_socks = remaining_socks - donated_socks + additional_socks

    result = total_socks
    return result

print(solution())