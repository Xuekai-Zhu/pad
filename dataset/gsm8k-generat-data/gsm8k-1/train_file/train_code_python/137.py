def solution():
    """A gallon of whole milk that normally costs $3 is now sold at $2. A box of cereal was sold at a discount of $1. How much will you save via discounts if you buy 3 gallons of whole milk and 5 boxes of cereal?"""
    milk_price = 3
    milk_discount = 1
    cereal_discount = 1
    milk_savings_per_gallon = milk_price - 2
    cereal_savings_per_box = cereal_discount
    total_milk_savings = milk_savings_per_gallon * 3
    total_cereal_savings = cereal_savings_per_box * 5
    total_savings = total_milk_savings + total_cereal_savings
    result = total_savings
    return result

print(solution())