def solution():
    """Suzanne sold 80 cookies for $1 each and 60 cupcakes for $4 each. She gave her two sisters $10 each for helping her. How much money does she have left from her earnings?"""
    cookies_sold = 80
    cookies_price = 1
    cupcakes_sold = 60
    cupcakes_price = 4
    sisters_money = 10 * 2
    earnings = (cookies_sold * cookies_price) + (cupcakes_sold * cupcakes_price)
    total_money = earnings - sisters_money
    result = total_money
    return result

print(solution())