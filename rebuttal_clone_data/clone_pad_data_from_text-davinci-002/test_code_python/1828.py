def solution():
    initial_investment = 1000
    monthly_investment = 100
    interest_rate = 10
    months = 24
    total_investment = initial_investment + (monthly_investment * months)
    interest_earned = total_investment * (interest_rate / 100)
    total_money = total_investment + interest_earned
    result = total_money
    return result

print(solution())