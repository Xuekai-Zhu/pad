def solution():
    
    total_beries = 30 + 20 + 10
    rotten_beries = total_beries / 3
    fresh_beries = total_beries - rotten_beries
    fresh_beries_kept = fresh_beries / 2
    berries_to_sell = fresh_beries - fresh_beries_kept
    result = berries_to_sell
    return result

print(solution())