def solution():
    
    mining_profit_per_year = 3000000 * 365
    refining_profit_per_year = 5000000 * 365
    total_profit_per_year = mining_profit_per_year + refining_profit_per_year
    expenses_per_year = 30000000 * 12
    net_profit_per_year = total_profit_per_year - expenses_per_year
    fine = net_profit_per_year * 0.01
    result = fine
    return result

print(solution())