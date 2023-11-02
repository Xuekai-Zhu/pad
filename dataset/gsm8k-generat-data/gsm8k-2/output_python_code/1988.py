def solution():
    """Yulia was able to net $44 in profit this week. Her lemonade stand made a gross revenue of $47 this week. She was also able to babysit and made $31. However, her lemonade stand is expensive to run because she needs to buy lemons, sugar, and sunscreen. How much did she spend to operate her lemonade stand, in dollars?"""
    gross_revenue = 47
    babysitting_income = 31
    net_profit = 44
    operating_expenses = gross_revenue + babysitting_income - net_profit
    result = operating_expenses
    return result

print(solution())