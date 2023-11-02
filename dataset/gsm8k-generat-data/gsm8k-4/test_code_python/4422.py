def solution():
    """A smartphone seller is offering a discount of 5% off for customers who buy at least 2 smartphones at once. Melinda, Zoe and Joel want to buy an iPhone X each. If an iPhone X costs $600, how much can they save by pooling their money together and buying three iPhones at once from this seller rather than buying individually?"""
    # Define the original price of one iPhone X
    original_price = 600

    # Calculate the price of three iPhone Xs without discount
    total_price_individual = original_price * 3

    # Calculate the price of three iPhone Xs with discount
    total_price_bulk = (original_price * 3) * 0.95

    # Calculate the amount saved by buying the iPhones in bulk
    amount_saved = total_price_individual - total_price_bulk

    # return the result
    result = amount_saved
    return result

print(solution())