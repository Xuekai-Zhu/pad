def solution():
    """A gallon of whole milk that normally costs $3 is now sold at $2. A box of cereal was sold at a discount of $1. How much will you save via discounts if you buy 3 gallons of whole milk and 5 boxes of cereal?"""
    # Define the original and discounted prices of milk and cereal
    milk_orig_price = 3
    milk_disc_price = 2
    cereal_orig_price = None
    cereal_disc_price = None

    # Define the discount amount for cereal
    cereal_discount = 1

    # Calculate the discounted price of cereal
    cereal_disc_price = cereal_orig_price - cereal_discount

    # Calculate the total savings from buying 3 gallons of milk and 5 boxes of cereal
    milk_savings = (milk_orig_price - milk_disc_price) * 3
    cereal_savings = cereal_discount * 5
    total_savings = milk_savings + cereal_savings

    # return the result
    result = total_savings
    return result

print(solution())