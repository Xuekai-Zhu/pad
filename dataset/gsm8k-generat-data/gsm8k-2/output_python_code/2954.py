def solution():
    """Mo is buying valentine's day cards for the class. There are 30 students and he wants to give a Valentine to 60% of them. They cost $2 each. If he has $40, what percentage of his money will he spend on Valentine?"""
    total_students = 30
    valentines_percent = 0.6
    valentines_to_buy = int(total_students * valentines_percent)
    valentine_cost = 2
    total_cost = valentines_to_buy * valentine_cost
    money_spent_percent = (total_cost / 40) * 100
    result = money_spent_percent
    return result

print(solution())