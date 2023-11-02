def solution():
    """A gallon of whole milk that normally costs $3 is now sold at $2. A box of cereal was sold at a discount of $1. How much will you save via discounts if you buy 3 gallons of whole milk and 5 boxes of cereal?"""
    milk_price = 3
    milk_discount_price = 2
    cereal_discount_price = 1
    total_milk_price = 3 * 3
    total_cereal_price = 5 * (milk_price - cereal_discount_price)
    total_discount = (total_milk_price - (3 * 2)) + total_cereal_price
    result = total_discount
    return result

print(solution())