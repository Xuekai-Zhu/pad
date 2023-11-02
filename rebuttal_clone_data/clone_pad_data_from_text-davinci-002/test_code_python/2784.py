def solution():
    money = 15
    cost_notebook = 4
    cost_pen = 1.5
    notebooks = 2
    pens = 2
    total_cost = notebooks * cost_notebook + pens * cost_pen
    money_left = money - total_cost
    result = money_left
    return result

print(solution())