def solution():
    """To get the printer to work, Jerry needs to add a black-and-white cartridge and three color cartridges. If each color cartridge costs $32 and each black-and-white cartridge costs $27, how much does he pay total?"""
    b_w_cartridge_cost = 27
    color_cartridge_cost = 32
    num_color_cartridges = 3
    total_cost = b_w_cartridge_cost + (color_cartridge_cost * num_color_cartridges)
    result = total_cost
    return result

print(solution())