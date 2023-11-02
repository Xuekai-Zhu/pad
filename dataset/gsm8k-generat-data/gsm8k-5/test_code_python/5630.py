def solution():
    hours_per_week = 40  # Sara worked 40 hours per week
    pay_per_hour = 11.50  # Sara earned $11.50 per hour
    weeks_worked = 2  # Sara worked for 2 weeks

    # Calculate the total pay before taxes and expenses
    total_pay = hours_per_week * pay_per_hour * weeks_worked

    # Subtract the cost of the new tires
    money_left = total_pay - 410
    result = money_left
    return result

print(solution())