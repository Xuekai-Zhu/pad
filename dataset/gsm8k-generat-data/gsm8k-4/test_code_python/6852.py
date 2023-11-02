def solution():
    """Mark has the option of getting a $300 lens with a 20% discount or a $220 lens. How much money does he save by buying the cheaper lens?"""
    # Define the price of the lens with the discount
    lens_discount_price = 300 * 0.8

    # Determine which lens is cheaper
    if lens_discount_price < 220:
        cheaper_lens = "discounted"
        price_difference = 220 - lens_discount_price
    else:
        cheaper_lens = "non-discounted"
        price_difference = 0

    result = price_difference
    return result

print(solution())