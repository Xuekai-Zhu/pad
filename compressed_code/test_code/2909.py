def solution():
    
    basic_price = 8
    scientific_price = 2 * basic_price
    graphing_price = 3 * scientific_price
    total_cost = (1 * basic_price) + (1 * scientific_price) + (1 * graphing_price)
    change = 100 - total_cost
    result = change
    return result

print(solution())