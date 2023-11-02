def solution():
    """Faye had $20. Today, her mother gave her twice as much as her money. If she bought ten cupcakes at $1.50 each and five boxes of cookies at $3 per box, how much money did she have left?"""
    initial_money = 20
    mother_money = initial_money * 2
    total_money = initial_money + mother_money
    cupcakes_cost = 10 * 1.5
    cookies_cost = 5 * 3
    total_cost = cupcakes_cost + cookies_cost
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())