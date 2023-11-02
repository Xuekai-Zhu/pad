def solution():
    """Uki owns a bakery. She sells cupcakes at $1.50 each, cookies at $2 per packet, and biscuits at $1 per packet. In a day, she can bake an average of twenty cupcakes, ten packets of cookies, and twenty packets of biscuits. How much will be her total earnings for five days?"""
    cupcakes_price = 1.5
    cookies_price = 2
    biscuits_price = 1
    cupcakes_per_day = 20
    cookies_per_day = 10
    biscuits_per_day = 20
    total_days = 5
    total_earnings = (cupcakes_price * cupcakes_per_day + cookies_price * cookies_per_day + biscuits_price * biscuits_per_day) * total_days
    result = total_earnings
    return result

print(solution())