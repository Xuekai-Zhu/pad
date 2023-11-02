def solution():
    """A store decides to shut down and sell all of its inventory. They have 2000 different items which would normally retail for $50.
    They are offering an 80% discount and manage to sell 90% of the items. They owed $15000 to their creditors. How much money do they have left after the sale?"""
    number_of_items = 2000
    retail_price = 50
    discount = 0.8
    sale_price = retail_price * (1 - discount)
    sold_percentage = 0.9
    revenue = number_of_items * retail_price * discount * sold_percentage
    debt = 15000
    left_money = revenue - debt
    result = left_money
    return result

print(solution())