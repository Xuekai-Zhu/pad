def solution():
    flowering_plants = 7  # Roxy has 7 flowering plants
    fruiting_plants = 2 * flowering_plants  # Roxy has twice as many fruiting plants as flowering plants
    nursery_plants = 3 + 2  # Roxy buys 3 flowering plants and 2 fruiting plants from the nursery
    given_away_plants = 1 + 4  # Roxy gives away 1 flowering plant and 4 fruiting plants

    # Calculate the total number of plants remaining in Roxy's garden
    remaining_plants = flowering_plants + fruiting_plants + nursery_plants - given_away_plants
    result = remaining_plants
    return result

print(solution())