def solution():
    original_investment = 80
    growth_rate = 15
    new_investment = 28
    final_growth_rate = 10
    year_one = original_investment + (original_investment * (growth_rate / 100))
    final_portfolio = year_one + new_investment + ((year_one + new_investment) * (final_growth_rate / 100))
    result = final_portfolio
    
    return result

print(solution())