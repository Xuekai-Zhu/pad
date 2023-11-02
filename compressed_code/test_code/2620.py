def solution():
    
    total_beries = 30 + 20 + 10
    rotten_beries = total_beries / 3
    fresh_beries = total_beries - rotten_beries
    sellable_beries = fresh_beries / 2
    result = sellable_beries
    return result

print(solution())