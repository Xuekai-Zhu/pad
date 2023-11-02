def solution():
    # Calculate the total amount of money Hannah earned from selling cookies
    cookies_money = 40 * 0.8

    # Calculate the total amount of money Hannah earned from selling cupcakes
    cupcakes_money = 30 * 2

    # Calculate the total amount of money Hannah earned
    total_money = cookies_money + cupcakes_money

    # Calculate the total cost of the measuring spoons
    measuring_spoons_cost = 2 * 6.5

    # Calculate the amount of money Hannah has left
    money_left = total_money - measuring_spoons_cost
    result = money_left
    return result

print(solution())