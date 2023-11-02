def solution():
    """The cost of purchasing two commodities is $827. If the purchase price of the first one exceeds the other by $127, what is the purchase price of the first commodity?"""
    total_cost = 827
    difference = 127
    first_commodity_price = (total_cost + difference) / 2
    result = first_commodity_price
    return result

print(solution())