def solution():
    """MegaCorp got caught leaking carcinogens into the water supply and is being fined 1% of its annual profits. Every day MegaCorp earns $3,000,000 from mining and $5,000,000 from oil refining. Its monthly expenses are $30,000,000. How much is MegaCorp's fine in dollars?"""
    mining_profit_per_year = 3000000 * 365
    refining_profit_per_year = 5000000 * 365
    total_profit_per_year = mining_profit_per_year + refining_profit_per_year
    expenses_per_year = 30000000 * 12
    net_profit_per_year = total_profit_per_year - expenses_per_year
    fine = net_profit_per_year * 0.01
    result = fine
    return result

print(solution())