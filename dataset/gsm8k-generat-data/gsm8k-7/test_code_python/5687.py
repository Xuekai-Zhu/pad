def solution():
    num_white_packs = 2
    white_pack_size = 5

    num_blue_packs = 4
    blue_pack_size = 3

    price_per_shirt = 3

    # Calculate the total number of white shirts
    total_white_shirts = num_white_packs * white_pack_size

    # Calculate the total number of blue shirts
    total_blue_shirts = num_blue_packs * blue_pack_size

    # Calculate the total cost of all shirts
    total_cost = (total_white_shirts + total_blue_shirts) * price_per_shirt
    result = total_cost
    return result

print(solution())