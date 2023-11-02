def solution():
    """A gallon of whole milk that normally costs $3 is now sold at $2. A box of cereal was sold at a discount of $1. How much will you save via discounts if you buy 3 gallons of whole milk and 5 boxes of cereal?"""
    milk_unit_price = 2
    milk_quantity = 3
    cereal_unit_price = 1
    cereal_quantity = 5
    total_savings = (milk_unit_price * milk_quantity) + (cereal_unit_price * cereal_quantity)
    result = total_savings
    
    return result

print(solution())