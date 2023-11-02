def solution():
    """To get the printer to work, Jerry needs to add a black-and-white cartridge and three color cartridges. If each color cartridge costs $32 and each black-and-white cartridge costs $27, how much does he pay total?"""
    # Define the cost of each type of cartridge
    COLOR_PRICE = 32
    BW_PRICE = 27

    # Define the number of cartridges needed
    color_cartridges = 3
    bw_cartridges = 1

    # Calculate the total cost of the color cartridges
    color_cost = color_cartridges * COLOR_PRICE

    # Calculate the total cost of the black-and-white cartridge
    bw_cost = bw_cartridges * BW_PRICE

    # Calculate the total cost of all the cartridges
    total_cost = color_cost + bw_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())