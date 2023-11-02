def solution():
    turquoise_price = 13.0
    purple_price = 11.0
    wall1_length = 5.0
    wall1_width = 8.0
    wall2_length = 7.0
    wall2_width = 8.0
    tiles_per_sq_ft = 4

    # Calculate the total number of tiles needed for wall 1
    wall1_tiles = wall1_length * wall1_width * tiles_per_sq_ft

    # Calculate the total number of tiles needed for wall 2
    wall2_tiles = wall2_length * wall2_width * tiles_per_sq_ft

    # Calculate the total number of tiles needed for both walls
    total_tiles = wall1_tiles + wall2_tiles

    # Calculate the cost of using the turquoise tiles
    turquoise_cost = total_tiles * turquoise_price

    # Calculate the cost of using the purple tiles
    purple_cost = total_tiles * purple_price

    # Calculate the amount that Janet would save by buying the purple tiles instead of the turquoise ones
    savings = turquoise_cost - purple_cost

    result = savings
    return result

print(solution())