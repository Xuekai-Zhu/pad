def solution():
    """Frances sells 20 cupcakes for $2 for each cupcake and 40 cookies at $1 each. She buys five trays at $4 for each tray. How much money does Frances have left?"""
    cupcakes_sold = 20
    cupcake_price = 2
    cookies_sold = 40 
    cookie_price = 1 
    trays_bought = 5
    tray_cost = 4
    total_earnings = (cupcakes_sold * cupcake_price) + (cookies_sold * cookie_price)
    total_cost = trays_bought * tray_cost
    money_left = total_earnings - total_cost
    result = money_left
    return result

print(solution())