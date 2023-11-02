def solution():
    """Kenneth spent 10% of his earnings this week on a new joystick. If he is left with $405, how much were his earnings?"""
    remaining_money = 405
    percent_spent = 10
    money_spent = remaining_money / (percent_spent / 100)
    total_earnings = remaining_money + money_spent
    result = total_earnings
    return result

print(solution())