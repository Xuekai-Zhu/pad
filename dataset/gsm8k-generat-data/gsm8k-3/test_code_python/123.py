def solution():
    """A bulk warehouse is offering 48 cans of sparkling water for $12.00 a case. The local grocery store is offering the same sparkling water for $6.00 and it only has 12 cans. How much more expensive, per can, in cents, is this deal at the grocery store?"""
    # Define the prices and quantities for both deals
    warehouse_price = 12.00
    warehouse_quantity = 48
    grocery_price = 6.00
    grocery_quantity = 12

    # Calculate the cost per can for both deals and convert to cents
    warehouse_per_can = (warehouse_price / warehouse_quantity) * 100
    grocery_per_can = (grocery_price / grocery_quantity) * 100

    # Calculate the difference in cost per can, in cents
    difference = warehouse_per_can - grocery_per_can

    # return the result
    result = difference
    return result

print(solution())