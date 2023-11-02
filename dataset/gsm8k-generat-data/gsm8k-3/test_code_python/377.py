def solution():
    """A store owner buys clothes wholesale and adds 80% to the wholesale price to set the retail price. The retail price of a pair of pants is $36. What is the wholesale price?"""
    # Define the markup percentage and the retail price of the pants
    MARKUP_PERCENTAGE = 0.8
    RETAIL_PRICE = 36

    # Calculate the wholesale price of the pants
    wholesale_price = RETAIL_PRICE / (1 + MARKUP_PERCENTAGE)

    # Display the wholesale price
    result = wholesale_price
    return result

print(solution())