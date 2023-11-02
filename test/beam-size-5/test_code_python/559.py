def solution():
    
    sons = 2
    candles_per_son = 12
    years_younger = 4
    candles_per_pack = 5
    cost_per_pack = 3
    total_candles = sons * candles_per_son + years_younger + candles_per_pack
    total_cost = total_candles * cost_per_pack
    result = total_cost
    return result

print(solution())