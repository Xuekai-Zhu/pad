def solution():
    """To get the printer to work, Jerry needs to add a black-and-white cartridge and three color cartridges. If each color cartridge costs $32 and each black-and-white cartridge costs $27, how much does he pay total?"""
    # Define the price of a black-and-white cartridge and a color cartridge
    BLACK_WHITE_PRICE = 27
    COLOR_PRICE = 32

    # Calculate the total cost of the cartridges
    total_cost = BLACK_WHITE_PRICE + (3 * COLOR_PRICE)

    # Return the result
    result = total_cost
    return result

print(solution())