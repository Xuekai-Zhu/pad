def solution():
    # Calculate the total revenue from cupcake sales
    cupcake_sales = 50 * 2

    # Calculate the total revenue from cookie sales
    cookie_sales = 40 * 0.5

    # Calculate the total revenue from all sales
    total_sales = cupcake_sales + cookie_sales

    # Calculate the cost of the two basketballs
    basketball_cost = 2 * 40

    # Calculate the remaining money after buying the basketballs
    remaining_money = total_sales - basketball_cost

    # Calculate the cost of one bottle of energy drink
    energy_drink_cost = remaining_money / 20

    result = energy_drink_cost
    return result

print(solution())