def solution():
    """Chad saves 40% of the money he earns/receives in a year. This year, he made $600 mowing yards and received $250.00 for his birthday/holidays. He also made $150.00 by selling some old video games and another $150.00 doing odd jobs. How much will he save?"""
    total_income = 600 + 250 + 150 + 150
    savings_percentage = 0.4
    total_savings = total_income * savings_percentage
    result = total_savings
    return result

print(solution())