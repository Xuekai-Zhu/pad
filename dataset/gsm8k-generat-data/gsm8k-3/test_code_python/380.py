def solution():
    """Uki owns a bakery. She sells cupcakes at $1.50 each, cookies at $2 per packet, and biscuits at $1 per packet. In a day, she can bake an average of twenty cupcakes, ten packets of cookies, and twenty packets of biscuits.  How much will be her total earnings for five days?"""
    # Define the prices of each item
    CUPCAKE_PRICE = 1.50
    COOKIE_PRICE = 2.00
    BISCUIT_PRICE = 1.00

    # Define the average daily production of each item
    CUPCAKE_PRODUCTION = 20
    COOKIE_PRODUCTION = 10
    BISCUIT_PRODUCTION = 20

    # Calculate the total earnings for one day
    daily_earnings = (CUPCAKE_PRICE * CUPCAKE_PRODUCTION) + (COOKIE_PRICE * COOKIE_PRODUCTION) + (BISCUIT_PRICE * BISCUIT_PRODUCTION)

    # Calculate the total earnings for five days
    total_earnings = daily_earnings * 5

    # Display the total earnings
    result = total_earnings
    return result

print(solution())