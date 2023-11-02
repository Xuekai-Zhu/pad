def solution():
    land_cost = 50 * 2000  # Land costs $50 per square meter and the house requires 2000 square meters
    brick_cost = 100 * (10000/1000)  # Bricks cost $100 per 1000 bricks and the house requires 10000 bricks
    roof_tile_cost = 10 * 500  # Roof tiles cost $10 per roof tile and the house requires 500 tiles
    
    # Calculate the total construction costs for the project
    total_cost = land_cost + brick_cost + roof_tile_cost
    result = total_cost
    return result

print(solution())