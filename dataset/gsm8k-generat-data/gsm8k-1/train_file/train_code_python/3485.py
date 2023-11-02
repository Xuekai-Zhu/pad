def solution():
    """Randy had some money. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. If Randy has $2000 left, how much money, in dollars, did Randy have at first?"""
    starting_money = (2000 + 1200) * 2
    result = starting_money - 200
    return result

print(solution())