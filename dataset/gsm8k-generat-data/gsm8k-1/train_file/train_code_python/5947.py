def solution():
    """A quantity surveyor is figuring the construction costs for a couple that wishes to build a house. The costs are as follows: land costs $50 per square meter, bricks cost $100 per 1000 bricks and roof tiles cost $10 per roof tile. If the house they wish to build requires 2000 square meters, 10000 bricks, and 500 roof tiles, how much construction costs are required for this project?"""
    land_cost = 50 * 2000
    brick_cost = 100 * (10000/1000)
    roof_tile_cost = 10 * 500
    total_cost = land_cost + brick_cost + roof_tile_cost
    result = total_cost
    return result

print(solution())