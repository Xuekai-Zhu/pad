def solution():
    num_color_cartridges = 3
    color_cartridge_price = 32

    num_bw_cartridges = 1
    bw_cartridge_price = 27

    # Calculate the total cost of all color cartridges
    total_color_cost = num_color_cartridges * color_cartridge_price

    # Calculate the total cost of the black-and-white cartridge
    total_bw_cost = num_bw_cartridges * bw_cartridge_price

    # Calculate the total cost of all cartridges
    total_cost = total_color_cost + total_bw_cost
    result = total_cost
    return result

print(solution())