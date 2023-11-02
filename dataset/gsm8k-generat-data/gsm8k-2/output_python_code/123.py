def solution():
    """A bulk warehouse is offering 48 cans of sparkling water for $12.00 a case. The local grocery store is offering the same sparkling water for $6.00 and it only has 12 cans. How much more expensive, per can, in cents, is this deal at the grocery store?"""
    bulk_price = 12.00
    bulk_cans = 48
    bulk_per_can = bulk_price / bulk_cans
    grocery_price = 6.00
    grocery_cans = 12
    grocery_per_can = grocery_price / grocery_cans
    difference_per_can = (grocery_per_can - bulk_per_can) * 100
    result = difference_per_can
    return result

print(solution())