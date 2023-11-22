def solution():
    
    cookies_sold = 80
    cookies_price = 1
    cupcakes_sold = 60
    cupcakes_price = 4
    helping_sisters_sold = 2
    helping_sisters_money = 10
    total_earnings = (cookies_sold * cookies_price) + (cupcakes_sold * cupcakes_price) + helping_sisters_money
    money_left = total_earnings - total_earnings
    result = money_left
    return result

print(solution())