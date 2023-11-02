def solution():
    starting_pebbles = 18
    skipped_pebbles = starting_pebbles / 2
    freddy_pebbles = 30

    # Calculate the total number of pebbles Marcus has now
    total_pebbles = starting_pebbles - skipped_pebbles + freddy_pebbles

    result = total_pebbles
    return result

print(solution())