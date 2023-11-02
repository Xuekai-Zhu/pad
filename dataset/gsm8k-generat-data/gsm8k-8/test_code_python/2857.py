def solution():
    # Calculate the total number of white T-shirts
    white_packs = 3
    white_per_pack = 6
    total_white = white_packs * white_per_pack

    # Calculate the total number of blue T-shirts
    blue_packs = 2
    blue_per_pack = 4
    total_blue = blue_packs * blue_per_pack

    # Calculate the total number of T-shirts
    total_tshirts = total_white + total_blue
    result = total_tshirts
    return result

print(solution())