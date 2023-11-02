def solution():
    """The basketball team sold 50 cupcakes for $2 each and 40 cookies for $0.5 each. Then the money from their sales was used to buy two basketballs that cost $40 each. The rest of the money was used to buy 20 bottles of energy drinks. How much does a bottle of energy drink cost?"""
    # Calculate the total revenue from selling cupcakes and cookies
    cupcakes_revenue = 50 * 2
    cookies_revenue = 40 * 0.5
    total_revenue = cupcakes_revenue + cookies_revenue

    # Calculate the total cost of the basketballs
    basketballs_cost = 2 * 40

    # Calculate the remaining money after buying the basketballs
    remaining_money = total_revenue - basketballs_cost

    # Calculate the cost of each bottle of energy drink
    energy_drink_cost = remaining_money / 20

    result = energy_drink_cost
    return result

print(solution())