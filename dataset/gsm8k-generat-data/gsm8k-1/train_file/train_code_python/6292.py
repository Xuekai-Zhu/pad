def solution():
    """John invests in a bank and gets 10% simple interest. He invests $1000. How much money does he have after 3 years?"""
    initial_investment = 1000
    interest_rate = 0.1
    investment_years = 3
    interest_earned = initial_investment * interest_rate * investment_years
    total_money = initial_investment + interest_earned
    result = total_money
    return result

print(solution())