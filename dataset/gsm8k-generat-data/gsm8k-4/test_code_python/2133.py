def solution():
    """The cost of purchasing two commodities is $827. If the purchase price of the first one exceeds the other by $127, what is the purchase price of the first commodity?"""
    # Define the total cost and the price difference between the two commodities
    total_cost = 827
    price_difference = 127

    # Calculate the purchase price of the second commodity
    second_commodity_price = (total_cost - price_difference) / 2

    # Calculate the purchase price of the first commodity
    first_commodity_price = second_commodity_price + price_difference

    # return the result
    result = first_commodity_price
    return result

print(solution())