def solution():
    """The basketball team sold 50 cupcakes for $2 each and 40 cookies for $0.5 each. Then the money from their sales was used to buy two basketballs that cost $40 each. The rest of the money was used to buy 20 bottles of energy drinks. How much does a bottle of energy drink cost?"""
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