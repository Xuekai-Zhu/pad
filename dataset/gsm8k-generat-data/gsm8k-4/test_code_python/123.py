def solution():
    """A bulk warehouse is offering 48 cans of sparkling water for $12.00 a case.  The local grocery store is offering the same sparkling water for $6.00 and it only has 12 cans.  How much more expensive, per can, in cents, is this deal at the grocery store?"""
    # Calculate the cost per can at the bulk warehouse
    bulk_price_per_can = 12 / 48

    # Calculate the cost per can at the local grocery store
    grocery_price_per_can = 6 / 12

    # Calculate the price difference per can between the two stores
    price_difference_per_can = (grocery_price_per_can - bulk_price_per_can) * 100

    # Convert the price difference to cents
    price_difference_per_can = round(price_difference_per_can * 100)

    # return the result
    result = price_difference_per_can
    return result

print(solution())