def solution():
    """A store decides to shut down and sell all of its inventory. They have 2000 different items which would normally retail for $50. They are offering an 80% discount and manage to sell 90% of the items. They owed $15000 to their creditors. How much money do they have left after the sale?"""
    # Define the original retail price of each item and the number of items
    retail_price = 50
    num_items = 2000

    # Calculate the total revenue if all items were sold at full price
    total_revenue = retail_price * num_items

    # Calculate the total revenue after the discount and the number of items sold
    discounted_price = retail_price * 0.2
    num_sold = num_items * 0.9
    total_revenue_discounted = discounted_price * num_sold

    # Calculate the amount owed to creditors and the total revenue after paying them off
    amount_owed = 15000
    revenue_after_creditors = total_revenue_discounted - amount_owed

    # Return the result
    result = revenue_after_creditors
    return result

print(solution())