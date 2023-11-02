def solution():
    """Randy had $3,000. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. What was the value, in dollars, of the rest?"""
    randy_money = 3000
    smith_money = 200
    sally_money = 1200
    total_money = randy_money + smith_money
    rest_money = total_money - sally_money
    result = rest_money
    return result

print(solution())