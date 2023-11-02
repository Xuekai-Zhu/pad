def solution():
    
    buying_price = 12
    selling_price = buying_price * 1.25
    num_pots = 150
    profit_per_pot = selling_price - buying_price
    total_profit = profit_per_pot * num_pots
    result = total_profit
    return result

print(solution())