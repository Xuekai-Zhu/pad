def solution():
    # Calculate the number of tiles needed for each wall
    tiles_1 = 5 * 8 * 4  # first wall measures 5 feet by 8 feet
    tiles_2 = 7 * 8 * 4  # second wall measures 7 feet by 8 feet

    # Calculate the total number of tiles needed
    total_tiles = tiles_1 + tiles_2

    # Calculate the cost of using turquoise tiles
    turquoise_cost = total_tiles * 13

    # Calculate the cost of using purple tiles
    purple_cost = total_tiles * 11

    # Calculate the amount saved by using purple tiles instead of turquoise tiles
    amount_saved = turquoise_cost - purple_cost

    result = amount_saved
    return result

print(solution())