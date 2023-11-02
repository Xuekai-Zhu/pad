def solution():
    
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