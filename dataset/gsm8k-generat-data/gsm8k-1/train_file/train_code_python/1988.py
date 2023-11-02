def solution():
    """Yulia was able to net $44 in profit this week. Her lemonade stand made a gross revenue of $47 this week. She was also able to babysit and made $31. However, her lemonade stand is expensive to run because she needs to buy lemons, sugar, and sunscreen. How much did she spend to operate her lemonade stand, in dollars?"""
    gross_revenue = 47
    net_profit = 44
    babysitting_income = 31
    expenses = gross_revenue - net_profit - babysitting_income
    result = expenses
    return result

print(solution())