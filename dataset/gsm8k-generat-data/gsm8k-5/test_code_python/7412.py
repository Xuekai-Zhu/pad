def solution():
    initial_pebbles = 18  # Marcus had 18 pebbles
    skipped_pebbles = initial_pebbles / 2  # Marcus skipped half of his initial pebbles across the lake
    new_pebbles = 30  # Freddy gave Marcus another 30 pebbles

    # Calculate the total number of pebbles Marcus has now
    total_pebbles = initial_pebbles - skipped_pebbles + new_pebbles
    result = total_pebbles
    return result

print(solution())