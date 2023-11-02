def solution():
    """Caroline has 40 pairs of socks. She loses 4 pairs of socks at the laundromat. Of the remaining pairs of socks, she donates two-thirds to the thrift store. Then she purchases 10 new pairs of socks, and she receives 3 new pairs of socks as a gift from her dad. How many pairs of socks does Caroline have in total?"""
    # Define the initial number of socks
    INITIAL_SOCKS = 40

    # Update the number of socks after losing some at the laundromat
    remaining_socks = INITIAL_SOCKS - 4

    # Donate two-thirds of the remaining socks to the thrift store
    donated_socks = remaining_socks * (2 / 3)

    # Calculate the remaining number of socks
    remaining_socks -= donated_socks

    # Add the new pairs of socks purchased and received as a gift
    remaining_socks += 10 + 3

    # Display the total number of socks Caroline has
    result = remaining_socks
    return result

print(solution())