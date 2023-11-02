def solution():
    """Hannah sold 40 pieces of cookies for $0.8 each and 30 cupcakes for $2 each. She used the money to buy 2 sets of measuring spoons for $6.5 each. How much money does she have left?"""
    cookies_sold = 40
    cookies_price = 0.8
    cupcakes_sold = 30
    cupcakes_price = 2
    measuring_spoons_sets = 2
    measuring_spoons_set_price = 6.5
    
    total_sales = (cookies_sold * cookies_price) + (cupcakes_sold * cupcakes_price)
    total_expenses = measuring_spoons_sets * measuring_spoons_set_price
    remaining_money = total_sales - total_expenses
    
    result = remaining_money
    return result

print(solution())