def solution():
    
    sam_rounds = [16, 16, 16, 16]
    jeff_rounds = [15, 13, 20, 8]
    total_skips = sum(jeff_rounds)
    num_rounds = len(jeff_rounds)
    avg_skips_per_round = total_skips / num_rounds
    result = avg_skips_per_round
    return result

print(solution())