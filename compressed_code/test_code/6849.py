def solution():
    
    total_caterpillars = 4 * 10
    successful_caterpillars = total_caterpillars * (1 - 0.4)
    butterflies = successful_caterpillars
    sale_price = 3
    total_profit = butterflies * sale_price
    result = total_profit
    return result

print(solution())