def solution():
    
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