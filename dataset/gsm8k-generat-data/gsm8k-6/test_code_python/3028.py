def solution():
    # Calculate the number of towers on Mark's beach
    mark_towers = 20 * 10

    # Calculate the number of sandcastles and towers on Jeff's beach
    jeff_castles = 20 * 3
    jeff_towers = jeff_castles * 5

    # Calculate the combined total number of sandcastles and towers
    total_sandcastles_and_towers = mark_towers + jeff_castles + jeff_towers
    result = total_sandcastles_and_towers
    return result

print(solution())