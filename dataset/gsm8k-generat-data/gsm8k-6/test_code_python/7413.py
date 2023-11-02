def solution():
    # Calculate the total profits earned by both companies
    total_profit = 60000 / 0.4  # company B receives 40% of the profits, so total profits = profit / 0.4
    
    # Calculate the amount of profit company A receives
    profit_A = total_profit * 0.6  # company A receives 60% of the profits
    
    result = profit_A
    return result

print(solution())