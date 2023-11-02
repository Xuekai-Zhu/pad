def solution():
    # Calculate the total amount of money Hannah earned
    total_cookie_sales = 40 * 0.8
    total_cupcake_sales = 30 * 2
    total_money = total_cookie_sales + total_cupcake_sales

    # Calculate the cost of the measuring spoons
    cost_of_spoons = 2 * 6.5

    # Calculate the amount of money Hannah has left
    money_left = total_money - cost_of_spoons
    result = money_left
    return result

print(solution())