def solution():
    """Randy had some money. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. If Randy has $2000 left, how much money, in dollars, did Randy have at first?"""
    smith_money = 200
    sally_money = 1200
    remaining_money = 2000
    initial_money = remaining_money + sally_money
    initial_money += smith_money
    result = initial_money
    return result

print(solution())