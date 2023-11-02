def solution():
    # Calculate the number of hits in the game
    hits = 50 / 3  # there are three times as many misses as hits

    # Calculate the total number of hits and misses in the game
    total_hits_misses = hits + 50  # 50 misses were given

    result = (hits, 50, total_hits_misses)
    return result

print(solution())