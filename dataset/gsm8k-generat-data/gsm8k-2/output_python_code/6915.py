def solution():
    """A store marks a book 30% above the cost. But during a sale, a 10% discount was given. If the book costs $50, what is the percent profit?"""
    cost = 50
    markup_percent = 30
    sale_percent = 10
    selling_price = cost + (cost * markup_percent/100)
    discounted_price = selling_price - (selling_price * sale_percent/100)
    profit = discounted_price - cost
    profit_percent = profit/cost * 100
    result = round(profit_percent)
    return result

print(solution())