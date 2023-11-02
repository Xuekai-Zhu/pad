def solution():
    """Uki owns a bakery. She sells cupcakes at $1.50 each, cookies at $2 per packet, and biscuits at $1 per packet. In a day, she can bake an average of twenty cupcakes, ten packets of cookies, and twenty packets of biscuits. How much will be her total earnings for five days?"""
    # Define the prices and quantities of each item
    CUPCAKE_PRICE = 1.5
    COOKIE_PRICE = 2
    BISCUIT_PRICE = 1
    CUPCAKE_QUANTITY = 20
    COOKIE_QUANTITY = 10
    BISCUIT_QUANTITY = 20

    # Calculate the total earnings for one day
    total_earnings_day = (CUPCAKE_PRICE * CUPCAKE_QUANTITY) + (COOKIE_PRICE * COOKIE_QUANTITY) + (BISCUIT_PRICE * BISCUIT_QUANTITY)

    # Calculate the total earnings for five days
    total_earnings_five_days = total_earnings_day * 5

    result = total_earnings_five_days
    return result

print(solution())