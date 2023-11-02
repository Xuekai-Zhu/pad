def solution():
    """Uki owns a bakery. She sells cupcakes at $1.50 each, cookies at $2 per packet, and biscuits at $1 per packet. In a day, she can bake an average of twenty cupcakes, ten packets of cookies, and twenty packets of biscuits. How much will be her total earnings for five days?"""
    cupcakes_per_day = 20
    cookies_per_day = 10
    biscuits_per_day = 20
    
    price_per_cupcake = 1.5
    price_per_cookie_packet = 2
    price_per_biscuit_packet = 1
    
    total_cupcake_sales = cupcakes_per_day * price_per_cupcake * 5
    total_cookie_sales = cookies_per_day * price_per_cookie_packet * 5
    total_biscuit_sales = biscuits_per_day * price_per_biscuit_packet * 5
    
    total_earnings = total_cupcake_sales + total_cookie_sales + total_biscuit_sales
    
    result = total_earnings
    
    return result

print(solution())