def solution():
    num_white_packs = 3
    num_blue_packs = 2
    white_pack_size = 6
    blue_pack_size = 4

    # Calculate the total number of white T-shirts
    total_white_shirts = num_white_packs * white_pack_size

    # Calculate the total number of blue T-shirts
    total_blue_shirts = num_blue_packs * blue_pack_size

    # Calculate the total number of T-shirts
    total_shirts = total_white_shirts + total_blue_shirts
    result = total_shirts
    return result

print(solution())