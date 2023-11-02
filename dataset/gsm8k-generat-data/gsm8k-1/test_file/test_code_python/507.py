def solution():
    """Gerald works at a daycare that pays him $30 every day. He worked for an entire week and spent a total of $100. How much does he have left?"""
    pay_per_day = 30
    days_worked = 7
    total_earned = pay_per_day * days_worked
    total_spent = 100
    money_left = total_earned - total_spent
    result = money_left
    return result

print(solution())