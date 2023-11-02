def solution():
    """Neil charges $5.00 to trim up each boxwood.  He charges $15.00 to trim it into a fancy shape.  The customer wants the entire 30 boxwood hedge trimmed up.  He has also asked for 4 specific boxwoods shaped into spheres.  How much will Neil charge?"""
    # Define the prices for trimming up and shaping boxwoods
    TRIM_PRICE = 5
    SHAPE_PRICE = 15

    # Define the number of boxwoods to be trimmed and shaped
    hedge_boxwoods = 30
    shaped_boxwoods = 4

    # Calculate the cost of trimming up the entire hedge
    trim_cost = hedge_boxwoods * TRIM_PRICE

    # Calculate the cost of shaping the 4 specific boxwoods
    shape_cost = shaped_boxwoods * SHAPE_PRICE

    # Calculate the total cost
    total_cost = trim_cost + shape_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())