def solution():
    
    cost_of_purchases = 75
    cost_of_shorts = 5 * 7
    cost_of_shoes = 2 * 10
    cost_of_tops = cost_of_purchases - cost_of_shorts - cost_of_shoes
    price_per_top = cost_of_tops / 4
    result = price_per_top

    return result

print(solution())