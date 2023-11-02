def solution():
    """The local salon offers mani/pedis for $40.00. They are running a Mother's day special and offering 25% off their regular rate. Charlotte is treating herself, her daughter and 3 granddaughters to a spa day. How much will Charlotte spend on 5 mani/pedis?"""
    # Define the original price and the discount
    ORIGINAL_PRICE = 40
    DISCOUNT = 0.25

    # Calculate the discounted price per mani/pedi
    discounted_price = ORIGINAL_PRICE * (1 - DISCOUNT)

    # Calculate the total cost for 5 mani/pedis
    total_cost = 5 * discounted_price

    result = total_cost
    return result

print(solution())