def solution():
    """James was doing some shopping in his favorite shop and he saw an offer on shoes that give him a second pair of shoes for half off the original price. He took the offer and took the first pair of shoes for $40 and the second one for $60. At the cashier, the lady told him that the offer applies strictly to the cheaper pair of shoes, and also that he was selected for an extra discount of a fourth off the total amount. How much money did James end up paying for both pairs of shoes?"""
    # Define the prices of the shoes
    first_shoe_price = 40
    second_shoe_price = 60

    # Calculate the price of the cheaper shoe after the half-off offer
    cheaper_shoe_price = min(first_shoe_price, second_shoe_price) / 2

    # Calculate the total price before the extra discount
    total_price_before_discount = first_shoe_price + second_shoe_price - min(first_shoe_price, second_shoe_price) + cheaper_shoe_price

    # Calculate the extra discount
    extra_discount = total_price_before_discount / 4

    # Calculate the final price after the extra discount
    final_price = total_price_before_discount - extra_discount

    # Return the result
    result = final_price
    return result

print(solution())