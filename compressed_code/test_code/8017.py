def solution():
    
    cost_per_magazine = 3
    selling_price_per_magazine = 3.5
    magazines_bought = 10
    profit_per_magazine = selling_price_per_magazine - cost_per_magazine
    total_profit = profit_per_magazine * magazines_bought
    result = total_profit
    return result

print(solution())