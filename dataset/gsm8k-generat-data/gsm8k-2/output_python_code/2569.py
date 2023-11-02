def solution():
    """Kenneth spent 10% of this earnings this week on a new joystick. If he is left with $405, how much were his earnings?"""
    remaining_amount = 405
    spent_percent = 0.1
    total_amount = remaining_amount / (1 - spent_percent)
    result = total_amount
    return result

print(solution())