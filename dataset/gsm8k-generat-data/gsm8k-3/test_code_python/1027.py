def solution():
    """John commissions an artist to make him a 9 by 13 drawing.  A black and white drawing that size would cost $160.  He wants a color drawing so that is 50% more expensive.  How much did he pay?"""
    # Define the cost of a black and white drawing that size
    BW_COST = 160

    # Calculate the cost of a color drawing that size
    COLOR_COST = BW_COST * 1.5

    # Display the total cost
    result = COLOR_COST
    return result

print(solution())