def solution():
    """A bulk warehouse is offering 48 cans of sparkling water for $12.00 a case. The local grocery store is offering the same sparkling water for $6.00 and it only has 12 cans. How much more expensive, per can, in cents, is this deal at the grocery store?"""
    bulk_can_price = 12 / 48
    grocery_can_price = 6 / 12
    difference_per_can = (grocery_can_price - bulk_can_price) * 100
    result = round(difference_per_can)
    return result

print(solution())