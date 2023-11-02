def solution():
    """A store owner buys clothes wholesale and adds 80% to the wholesale price to set the retail price. The retail price of a pair of pants is $36. What is the wholesale price?"""
    # Define the retail price and the markup percentage
    retail_price = 36
    markup_percentage = 80

    # Calculate the multiplier for the markup percentage
    markup_multiplier = 1 + markup_percentage / 100

    # Calculate the wholesale price using the markup multiplier
    wholesale_price = retail_price / markup_multiplier

    result = round(wholesale_price, 2)
    return result

print(solution())