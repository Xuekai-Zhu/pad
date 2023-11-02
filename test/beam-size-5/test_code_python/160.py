def solution():
    # Calculate the total amount of money Jackie will have if she hires the accountant
    total_freelance_hours = 90 / 3  # she losing $35/hour in missed income
    total_missed_income = 35  # she losing $35/hour in missed income
    total_money = total_freelance_hours + total_missed_income

    # Calculate how much more money Jackie will have if she hires the accountant
    extra_money = 90 - total_money
    result = extra_money
    return result

print(solution())