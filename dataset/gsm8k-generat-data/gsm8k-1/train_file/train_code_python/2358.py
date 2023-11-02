def solution():
    """Joshua bought 25 oranges for $12.50. If he sells each one for 60c, how much profit in cents will he make on each orange?"""
    oranges_bought = 25
    cost = 1250  # cost in cents
    price_each = 60  # price in cents
    profit_each = price_each - (cost / oranges_bought)
    result = profit_each
    return result

print(solution())