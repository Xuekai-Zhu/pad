def solution():
    mark_sandcastles = 20
    mark_towers_per_castle = 10
    jeff_sandcastles = 3 * mark_sandcastles
    jeff_towers_per_castle = 5

    # Calculate the total number of sandcastles on both beaches
    total_sandcastles = mark_sandcastles + jeff_sandcastles

    # Calculate the total number of towers on Mark's beach
    mark_total_towers = mark_sandcastles * mark_towers_per_castle

    # Calculate the total number of towers on Jeff's beach
    jeff_total_towers = jeff_sandcastles * jeff_towers_per_castle

    # Calculate the combined total number of sandcastles and towers on both beaches
    combined_total = total_sandcastles + mark_total_towers + jeff_total_towers
    result = combined_total
    return result.

print(solution())