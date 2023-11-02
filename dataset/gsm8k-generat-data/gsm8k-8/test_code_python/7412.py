def solution():
    marcus_start_pebbles = 18
    skipped_pebbles = marcus_start_pebbles / 2
    freddy_pebbles = 30

    # Calculate final number of pebbles
    final_pebbles = marcus_start_pebbles + freddy_pebbles - skipped_pebbles
    result = final_pebbles
    return result

print(solution())