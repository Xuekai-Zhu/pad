def solution():
    # Calculate the total construction costs for the project
    land_cost = 50 * 2000  # land costs $50 per square meter for 2000 square meters of land
    brick_cost = 100 * (10000/1000)  # bricks cost $100 per 1000 bricks and 10000 bricks are required
    tile_cost = 10 * 500  # roof tiles cost $10 per tile and 500 tiles are required
    total_cost = land_cost + brick_cost + tile_cost
    result = total_cost
    return result

print(solution())