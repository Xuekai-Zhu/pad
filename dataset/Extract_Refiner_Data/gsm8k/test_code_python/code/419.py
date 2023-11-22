def solution():
    
    tattered_cost = 28
    jogger_cost = tattered_cost - 6
    total_saved = 6
    savings_from_jogger_jeans = total_saved / 3
    savings_from_tattered_jeans = tattered_cost - savings_from_jogger_jeans
    difference = savings_from_jogger_jeans - savings_from_tattered_jeans
    result = difference
    return result

print(solution())