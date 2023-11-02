def solution():
    """A store decides to shut down and sell all of its inventory.  They have 2000 different items which would normally retail for $50.  They are offering an 80% discount and manage to sell 90% of the items.  They owed $15000 to their creditors.  How much money do they have left after the sale?"""
    # Define the original retail price and discount percentage
    ORIGINAL_PRICE = 50
    DISCOUNT_PERCENTAGE = 0.8

    # Calculate the discounted price
    discounted_price = ORIGINAL_PRICE * DISCOUNT_PERCENTAGE

    # Calculate the total revenue from the sale
    total_revenue = discounted_price * 0.9 * 2000

    # Calculate the amount owed to creditors
    amount_owed = 15000

    # Calculate the amount of money left after paying off creditors
    money_left = total_revenue - amount_owed

    # Display the amount of money left
    result = money_left
    return result

print(solution())