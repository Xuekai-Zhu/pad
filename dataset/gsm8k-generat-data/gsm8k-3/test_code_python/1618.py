def solution():
    """James was doing some shopping in his favorite shop and he saw an offer on shoes that give him a second pair of shoes for half off the original price. He took the offer and took the first pair of shoes for $40 and the second one for $60. At the cashier, the lady told him that the offer applies strictly to the cheaper pair of shoes, and also that he was selected for an extra discount of a fourth off the total amount. How much money did James end up paying for both pairs of shoes?"""
    # Define the prices of the two pairs of shoes
    price1 = 40
    price2 = 60

    # Calculate the discounted price of the cheaper pair of shoes
    if price1 < price2:
        discount_price = price1 * 0.5
        regular_price = price2
    else:
        discount_price = price2 * 0.5
        regular_price = price1

    # Calculate the total price before the extra discount
    total_price = regular_price + discount_price

    # Calculate the extra discount
    extra_discount = total_price * 0.25

    # Calculate the final price
    final_price = total_price - extra_discount

    # Display the final price
    result = final_price
    return result

print(solution())