def solution():
    """A tub of ice cream costing $13 is now sold at $11. A packet of milk was sold at a discount of $0.5. How much will you save if you buy 2 tubs of ice cream and 4 packets of milk?"""
    ice_cream_price = 13
    ice_cream_discounted_price = 11
    milk_price = 1.5
    milk_discount = 0.5
    total_savings = (ice_cream_price - ice_cream_discounted_price) * 2 + (milk_discount) * 4
    result = total_savings
    return result

print(solution())