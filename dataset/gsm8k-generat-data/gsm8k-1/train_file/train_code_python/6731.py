def solution():
    """Nancy's ex owes her child support. He's supposed to pay 30% of his income each year. For 3 years, he made $30,000/year, then he got a 20% raise for the next four years. If he's only ever paid $1,200, how much does he owe her?"""
    years_30k = 3
    years_raise = 4
    income_30k = 30000
    raise_percent = 20
    paid_amount = 1200
    
    # calculate total income during 4 years of raise
    total_income_raise = (income_30k * (1 + raise_percent/100)) * years_raise
    
    # calculate total income during 3 years of 30k income
    total_income_30k = income_30k * years_30k
    
    # calculate total income over all 7 years
    total_income = total_income_raise + total_income_30k
    
    # calculate total owed to Nancy
    total_owed = total_income * 0.3 - paid_amount
    
    result = total_owed
    return result

print(solution())