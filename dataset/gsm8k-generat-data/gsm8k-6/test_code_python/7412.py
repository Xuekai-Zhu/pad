def solution():
    # Calculate the number of pebbles Marcus has after skipping half of them across the lake
    remaining_pebbles = 18 // 2  # integer division to get number of remaining pebbles
    total_pebbles = remaining_pebbles + 30  # add the 30 pebbles Freddy gave him
    result = total_pebbles
    return result

print(solution())