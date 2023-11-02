def solution():
    """Neil charges $5.00 to trim up each boxwood. He charges $15.00 to trim it into a fancy shape. The customer wants the entire 30 boxwood hedge trimmed up. He has also asked for 4 specific boxwoods shaped into spheres. How much will Neil charge?"""
    # Define the prices for trimming up and shaping boxwoods
    TRIM_PRICE = 5.00
    SHAPE_PRICE = 15.00

    # Define the number of boxwoods to be trimmed up and shaped
    NUM_TRIM = 30
    NUM_SHAPE = 4

    # Calculate the cost of trimming up all the boxwoods
    trim_cost = NUM_TRIM * TRIM_PRICE

    # Calculate the cost of shaping the specific boxwoods
    shape_cost = NUM_SHAPE * SHAPE_PRICE

    # Calculate the total cost for Neil's services
    total_cost = trim_cost + shape_cost

    result = total_cost
    return result

print(solution())