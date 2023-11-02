def solution():
    """A smartphone seller is offering a discount of 5% off for customers who buy at least 2 smartphones at once. Melinda, Zoe and Joel want to buy an iPhone X each. If an iPhone X costs $600, how much can they save by pooling their money together and buying three iPhones at once from this seller rather than buying individually?"""
    # Define the price of an iPhone X and the discount percentage
    IPHONE_PRICE = 600
    DISCOUNT_PERCENTAGE = 5

    # Calculate the total price of three iPhones individually
    individual_price = IPHONE_PRICE * 3

    # Calculate the total price of three iPhones with the discount
    discounted_price = IPHONE_PRICE * 3 * 0.95

    # Calculate the amount saved by buying three iPhones at once
    amount_saved = individual_price - discounted_price

    # Display the amount saved
    result = amount_saved
    return result

print(solution())