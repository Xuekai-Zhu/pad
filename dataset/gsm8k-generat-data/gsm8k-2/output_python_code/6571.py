def solution():
    """Josh’s mom gives him $20 to go shopping at the mall. He buys a hat for $10 and a pencil for $2. Then he buys four cookies. If each cookie costs $1.25, how much money does Josh have left?"""
    initial_money = 20
    hat_cost = 10
    pencil_cost = 2
    cookie_cost = 1.25
    total_spent = hat_cost + pencil_cost + (4 * cookie_cost)
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())