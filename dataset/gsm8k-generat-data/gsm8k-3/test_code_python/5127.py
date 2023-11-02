def solution():
    """The Early Bird Dinner offered dinner meals at half off the menu price if you eat between 2-4 pm.  Curtis ordered the Salisbury Steak that costs $16.00 and Rob ordered the Chicken Fried Steak at $18.00.  If they ate at 3 pm, what was the cost of their total bill?"""
    # Define the menu prices of the ordered dishes
    SALISBURY_PRICE = 16.00
    CHICKEN_FRIED_PRICE = 18.00

    # Calculate the discounted prices of the ordered dishes
    discounted_salisbury_price = 0.5 * SALISBURY_PRICE
    discounted_chicken_fried_price = 0.5 * CHICKEN_FRIED_PRICE

    # Calculate the total bill
    total_bill = discounted_salisbury_price + discounted_chicken_fried_price

    # Display the total bill
    result = total_bill
    return result

print(solution())