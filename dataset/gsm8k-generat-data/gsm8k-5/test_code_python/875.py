def solution():
    num_color_cartridges = 3
    cost_color_cartridge = 32
    cost_bw_cartridge = 27

    # Calculate the total cost of the color cartridges
    total_color_cost = num_color_cartridges * cost_color_cartridge

    # Calculate the cost of the black-and-white cartridge
    bw_cost = cost_bw_cartridge

    # Calculate the total cost
    total_cost = total_color_cost + bw_cost
    result = total_cost
    return result

print(solution())