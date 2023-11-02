def solution():
    """Hannah sold 40 pieces of cookies for $0.8 each and 30 cupcakes for $2 each. She used the money to buy 2 sets of measuring spoons for $6.5 each. How much money does she have left?"""
    cookie_price = 0.8
    cupcakes_price = 2
    cookie_quantity = 40
    cupcakes_quantity = 30
    measuring_spoons_price = 6.5
    measuring_spoons_quantity = 2
    
    total_cookies_sold = cookie_quantity * cookie_price
    total_cupcakes_sold = cupcakes_quantity * cupcakes_price
    total_expenses = measuring_spoons_price * measuring_spoons_quantity
    
    total_money = total_cookies_sold + total_cupcakes_sold
    money_left = total_money - total_expenses
    
    result = money_left
    return result

print(solution())