def solution():
    """A store is having an anniversary sale. A tub of ice cream costs $2 less than its original price of $12 and the juice is sold at $2 for 5 cans. How much will you pay if you buy two tubs of ice cream and 10 cans of juice?"""
    # Define the original price of the ice cream and the discount amount
    ORIGINAL_PRICE = 12
    DISCOUNT_AMOUNT = 2

    # Calculate the sale price of the ice cream
    ice_cream_price = ORIGINAL_PRICE - DISCOUNT_AMOUNT

    # Calculate the total cost of the ice cream
    ice_cream_cost = 2 * ice_cream_price

    # Calculate the total cost of the juice
    juice_cost = (10 // 5) * 2 + (10 % 5) * 0.4

    # Calculate the total cost of the purchase
    total_cost = ice_cream_cost + juice_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())