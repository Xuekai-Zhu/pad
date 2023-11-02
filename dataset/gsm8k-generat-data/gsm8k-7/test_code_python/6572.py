def solution():
    total_money = 20
    hat_cost = 10
    pencil_cost = 2
    num_cookies = 4
    cookie_cost = 1.25

    # Calculate the total cost of all items
    total_cost = hat_cost + pencil_cost + (num_cookies * cookie_cost)

    # Calculate how much money Josh has left
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())