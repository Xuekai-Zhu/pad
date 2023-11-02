def solution():
    """A quantity surveyor is figuring the construction costs for a couple that wishes to build a house. The costs are as follows: land costs $50 per square meter, bricks cost $100 per 1000 bricks and roof tiles cost $10 per roof tile. If the house they wish to build requires 2000 square meters, 10000 bricks, and 500 roof tiles, how much construction costs are required for this project?"""
    # Define the cost per unit of land, bricks, and roof tiles
    land_cost_per_meter = 50
    brick_cost_per_thousand = 100
    roof_tile_cost_per_tile = 10

    # Define the number of units of land, bricks, and roof tiles required for the house
    land_units = 2000
    brick_units = 10000
    roof_tile_units = 500

    # Calculate the total cost of land
    land_cost = land_cost_per_meter * land_units

    # Calculate the total cost of bricks
    brick_cost = (brick_units / 1000) * brick_cost_per_thousand

    # Calculate the total cost of roof tiles
    roof_tile_cost = roof_tile_cost_per_tile * roof_tile_units

    # Calculate the total construction cost
    total_cost = land_cost + brick_cost + roof_tile_cost
    result = total_cost
    return result

print(solution())