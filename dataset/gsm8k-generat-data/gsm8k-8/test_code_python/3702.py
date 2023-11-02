def solution():
    # Calculate the total area of the walls
    wall1_area = 5 * 8
    wall2_area = 7 * 8
    total_area = wall1_area + wall2_area

    # Calculate the number of tiles needed for turquoise and purple
    turquoise_tiles = total_area * 4
    purple_tiles = total_area * 4

    # Calculate the cost for turquoise and purple
    turquoise_cost = turquoise_tiles * 13
    purple_cost = purple_tiles * 11

    # Calculate the savings
    savings = turquoise_cost - purple_cost
    result = savings
    return result

print(solution())