def solution():
    """Erwan went on shopping. He purchased a pair of shoes at $200 but discounted 30%, and two shirts at $80 each. Upon checkout, the cashier said that there is an additional 5% discount. How much did he spend after all the discounts?"""
    # Define the original prices of the items
    SHOE_PRICE = 200
    SHIRT_PRICE = 80

    # Calculate the discounted price of the shoes
    shoe_discount = 0.3
    discounted_shoe_price = SHOE_PRICE - (SHOE_PRICE * shoe_discount)

    # Calculate the total cost of the two shirts
    shirt_cost = 2 * SHIRT_PRICE

    # Calculate the total cost of all items before the additional discount
    total_cost = discounted_shoe_price + shirt_cost

    # Calculate the additional discount
    additional_discount = 0.05
    final_cost = total_cost - (total_cost * additional_discount)

    # Display the final cost after all the discounts
    result = final_cost
    return result

print(solution())