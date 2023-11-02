def solution():
    
    cupcakes_sold = 50
    cupcake_price = 2
    cookies_sold = 40
    cookie_price = 0.5
    total_sales = (cupcakes_sold * cupcake_price) + (cookies_sold * cookie_price)
    basketball_cost = 40 * 2
    remaining_money = total_sales - basketball_cost
    energy_drinks_bought = 20
    energy_drink_cost = remaining_money / energy_drinks_bought
    result = energy_drink_cost
    return result

print(solution())