def solution():
    # Calculate the number of fruiting plants Roxy has
    fruiting_plants = 2 * 7  # Roxy has twice as many fruiting plants as flowering plants

    # Calculate the total number of plants Roxy has before buying and giving away
    total_plants = flowering_plants + fruiting_plants

    # Calculate the total number of plants Roxy has after buying and giving away
    total_plants = total_plants + 3 + 2 - 1 - 4  # Roxy buys 3 flowering plants and 2 fruiting plants, gives away 1 flowering and 4 fruiting

    result = total_plants
    return result

print(solution())