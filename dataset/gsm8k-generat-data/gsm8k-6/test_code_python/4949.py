def solution():
    # Calculate the profit made on each pot of lily of the valley
    cost_per_pot = 12 
    selling_price_per_pot = cost_per_pot * 1.25 
    profit_per_pot = selling_price_per_pot - cost_per_pot 

    # Calculate the total profit made from selling 150 pots of lily of the valley
    number_of_pots = 150 
    total_profit = profit_per_pot * number_of_pots 

    result = total_profit
    return result

print(solution())