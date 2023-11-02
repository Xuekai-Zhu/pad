def solution():
    
    cookies_sold = 80
    cookies_price = 1
    cupcakes_sold = 60
    cupcakes_price = 4
    sisters_given = 2 * 10
    total_earnings = (cookies_sold * cookies_price) + (cupcakes_sold * cupcakes_price)
    money_left = total_earnings - sisters_given
    result = money_left
    return result

print(solution())