def solution():
    # Calculate the area of the first wall
    area_1 = 5 * 8  # 5 feet by 8 feet

    # Calculate the area of the second wall
    area_2 = 7 * 8  # 7 feet by 8 feet

    # Calculate the total area to be tiled
    total_area = area_1 + area_2

    # Calculate the number of tiles required for each square foot of wall
    tiles_per_sf = 4

    # Calculate the total number of tiles required for the entire bathroom
    total_tiles = total_area * tiles_per_sf

    # Calculate the cost of the turquoise tiles
    turquoise_price = 13

    # Calculate the cost of the purple tiles
    purple_price = 11

    # Calculate the total cost of the turquoise tiles
    turquoise_cost = total_tiles * turquoise_price

    # Calculate the total cost of the purple tiles
    purple_cost = total_tiles * purple_price

    # Calculate the amount saved by choosing the purple tiles
    savings = turquoise_cost - purple_cost
    result = savings
    return result

print(solution())