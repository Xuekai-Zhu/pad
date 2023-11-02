def solution():
    """A store decides to shut down and sell all of its inventory. They have 2000 different items which would normally retail for $50. They are offering an 80% discount and manage to sell 90% of the items. They owed $15000 to their creditors. How much money do they have left after the sale?"""
    num_items = 2000
    retail_price = 50
    discount_percent = 80
    sell_percent = 90
    sale_price = retail_price * (100 - discount_percent) / 100
    revenue = num_items * sale_price * sell_percent / 100
    remaining_money = revenue - 15000
    result = remaining_money
    return result

print(solution())