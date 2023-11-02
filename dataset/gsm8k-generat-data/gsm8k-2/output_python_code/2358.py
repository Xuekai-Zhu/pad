def solution():
    """Joshua bought 25 oranges for $12.50. If he sells each one for 60c, how much profit in cents will he make on each orange?"""
    oranges = 25
    cost = 1250 # in cents
    selling_price = 60 # in cents
    revenue = selling_price * oranges
    profit = revenue - cost
    profit_per_orange = profit / oranges
    result = profit_per_orange
    return result

print(solution())