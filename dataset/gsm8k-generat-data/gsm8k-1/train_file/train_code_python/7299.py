def solution():
    """John's neighbor tells him to walk his dog for 1 hour each day for a total of $10. He does this for April, save for the 4 Sundays in April. He later spent $50 on books and gave his sister Kaylee the same amount. How much money did John have left?"""
    daily_pay = 10 / 26
    days_worked = 26 - 4
    total_pay = daily_pay * days_worked
    expenses = 50 + 50
    money_left = total_pay - expenses
    result = money_left
    return result

print(solution())