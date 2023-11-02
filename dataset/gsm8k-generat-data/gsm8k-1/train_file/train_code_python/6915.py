def solution():
    """A store marks a book 30% above the cost. But during a sale, a 10% discount was given. If the book costs $50, what is the percent profit?"""
    cost = 50
    markup_percent = 30
    sale_percent = 10
    marked_up_price = cost * (1 + (markup_percent / 100))
    sale_price = marked_up_price * (1 - (sale_percent / 100))
    profit = sale_price - cost
    profit_percent = (profit / cost) * 100
    result = profit_percent
    return result

print(solution())