def solution():
    """A store is having an anniversary sale. A tub of ice cream costs $2 less than its original price of $12 and the juice is sold at $2 for 5 cans. How much will you pay if you buy two tubs of ice cream and 10 cans of juice?"""
    # Define the original price of a tub of ice cream and the price during the sale
    original_ice_cream_price = 12
    sale_ice_cream_price = 12 - 2

    # Define the price of 5 cans of juice during the sale
    juice_price = 2

    # Calculate the cost of two tubs of ice cream and 10 cans of juice
    total_cost = (2 * sale_ice_cream_price) + ((10 // 5) * 2 * juice_price) + ((10 % 5) * (juice_price / 5))

    # Return the result
    result = round(total_cost, 2)
    return result

print(solution())