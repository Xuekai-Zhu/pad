def solution():
    """John's neighbor tells him to walk his dog for 1 hour each day for a total of $10. He does this for April, save for the 4 Sundays in April. He later spent $50 on books and gave his sister Kaylee the same amount. How much money did John have left?"""
    daily_pay = 10 / 26  # number of days in April excluding Sundays
    total_pay = daily_pay * 22  # number of days in April excluding Sundays
    total_expenses = 50 + 50  # $50 on books and another $50 given to sister
    remaining_money = total_pay - total_expenses
    result = remaining_money
    return result

print(solution())