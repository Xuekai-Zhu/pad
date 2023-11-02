def solution():
    num_misses = 50  # Given that there are 50 misses in the game
    hits_to_misses_ratio = 1/3  # Given that there are three times as many misses as hits

    # Calculate the number of hits in the game
    num_hits = num_misses * hits_to_misses_ratio

    # Calculate the total number of hits and misses in the game
    total_hits_and_misses = num_hits + num_misses
    result = (num_hits, num_misses, total_hits_and_misses)
    return result

print(solution())