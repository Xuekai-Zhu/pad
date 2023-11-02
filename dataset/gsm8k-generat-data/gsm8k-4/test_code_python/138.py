def solution():
    """A gallon of whole milk that normally costs $3 is now sold at $2. A box of cereal was sold at a discount of $1. How much will you save via discounts if you buy 3 gallons of whole milk and 5 boxes of cereal?"""
    # Define the original and discounted prices
    milk_original_price = 3
    milk_discounted_price = 2
    cereal_discount = 1

    # Calculate the savings on the milk purchases
    milk_savings = (milk_original_price - milk_discounted_price) * 3

    # Calculate the savings on the cereal purchases
    cereal_savings = cereal_discount * 5

    # Calculate the total savings
    total_savings = milk_savings + cereal_savings

    # return the result
    result = total_savings
    return result

print(solution())