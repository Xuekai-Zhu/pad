def solution():
    """John commissions an artist to make him a 9 by 13 drawing. A black and white drawing that size would cost $160. He wants a color drawing so that is 50% more expensive. How much did he pay?"""
    # Define the cost of a black and white drawing
    bw_cost = 160

    # Calculate the cost of a color drawing
    color_cost = bw_cost * 1.5

    # Return the total cost
    result = color_cost
    return result

print(solution())