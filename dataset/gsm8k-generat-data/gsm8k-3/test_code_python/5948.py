def solution():
    """A quantity surveyor is figuring the construction costs for a couple that wishes to build a house. The costs are as follows: land costs $50 per square meter, bricks cost $100 per 1000 bricks and roof tiles cost $10 per roof tile. If the house they wish to build requires 2000 square meters, 10000 bricks, and 500 roof tiles, how much construction costs are required for this project?"""
    # Define the cost per unit
    LAND_COST = 50
    BRICK_COST = 100 / 1000  # convert to cost per brick
    TILE_COST = 10

    # Define the required units
    land = 2000
    bricks = 10000
    tiles = 500

    # Calculate the total cost
    total_cost = (land * LAND_COST) + (bricks * BRICK_COST) + (tiles * TILE_COST)

    # Display the total cost
    result = total_cost
    return result

print(solution())