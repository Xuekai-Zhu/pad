def solution():
    num_cupcakes = 50
    cupcakes_price = 2

    num_cookies = 40
    cookies_price = 0.5

    basketball_price = 40

    # Calculate the total revenue from selling cupcakes
    cupcakes_revenue = num_cupcakes * cupcakes_price

    # Calculate the total revenue from selling cookies
    cookies_revenue = num_cookies * cookies_price

    # Calculate the total revenue from selling all items
    total_revenue = cupcakes_revenue + cookies_revenue

    # Calculate the total cost of buying two basketballs
    basketball_cost = 2 * basketball_price

    # Calculate the remaining amount of money after buying the basketballs
    remaining_money = total_revenue - basketball_cost

    num_energy_drinks = 20

    # Calculate the cost of one bottle of energy drink
    energy_drink_cost = remaining_money / num_energy_drinks
    result = energy_drink_cost
    return result

print(solution())