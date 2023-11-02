def solution():
    ties = 34
    belts = 40
    black_shirts = 63
    white_shirts = 42
    total_shirts = black_shirts + white_shirts
    jeans = total_shirts * (2/3)
    total_ties_and_belts = ties + belts
    scarves = total_ties_and_belts * (1/2)
    result = jeans - scarves
    return result

print(solution())