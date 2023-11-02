def solution():
    items = 2000  # The store has 2000 items
    retail_price = 50  # The retail price of each item is $50
    discount = 0.8  # The store is offering an 80% discount
    sell_percentage = 0.9  # The store manages to sell 90% of the items
    creditors = 15000  # The store owed $15000 to their creditors

    # Calculate the total revenue from the sale
    revenue = items * retail_price * discount * sell_percentage

    # Calculate the remaining amount of money after paying off creditors
    remaining_money = revenue - creditors
    result = remaining_money
    return result

print(solution())