def solution():
    # Calculate the total amount of money Faye has after her mother gives her twice her original amount
    faye_money = 20
    faye_money += 2 * faye_money

    # Calculate the cost of the cupcakes and cookies
    cupcakes_cost = 10 * 1.5
    cookies_cost = 5 * 3

    # Calculate the amount of money Faye has left
    faye_money -= cupcakes_cost + cookies_cost
    result = faye_money
    return result

print(solution())