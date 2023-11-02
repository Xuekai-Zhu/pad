def solution():
    land_cost_per_sqm = 50
    bricks_cost_per_thousand = 100
    roof_tile_cost = 10

    land_cost = land_cost_per_sqm * 2000
    bricks_cost = bricks_cost_per_thousand * 10
    roof_tiles_cost = roof_tile_cost * 500

    # Calculate the total construction cost
    total_cost = land_cost + bricks_cost + roof_tiles_cost
    result = total_cost
    return result

print(solution())