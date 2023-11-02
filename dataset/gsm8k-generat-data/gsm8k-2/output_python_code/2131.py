def solution():
    """The basketball team sold 50 cupcakes for $2 each and 40 cookies for $0.5 each. Then the money from their sales was used to buy two basketballs that cost $40 each. The rest of the money was used to buy 20 bottles of energy drinks. How much does a bottle of energy drink cost?"""
    cupcakes_sold = 50
    cupcakes_price = 2
    cookies_sold = 40
    cookies_price = 0.5
    basketball_price = 40
    total_sales = (cupcakes_sold * cupcakes_price) + (cookies_sold * cookies_price)
    remaining_money = total_sales - (2 * basketball_price)
    energy_drinks_bought = 20
    energy_drink_price = remaining_money / energy_drinks_bought
    result = energy_drink_price
    return result

print(solution())