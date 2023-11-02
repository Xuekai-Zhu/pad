def solution():
    normal_pay_rate = 12  # Gary's normal hourly pay rate
    overtime_pay_rate = normal_pay_rate * 1.5  # Gary's overtime hourly pay rate
    total_pay = 696  # Gary's total pay before taxes are taken out
    normal_hours = 40  # number of normal hours in a week
    # Calculate the number of overtime hours worked by Gary
    overtime_hours = (total_pay - normal_pay_rate * normal_hours) / (overtime_pay_rate - normal_pay_rate)
    total_hours = normal_hours + overtime_hours
    result = total_hours
    return result

print(solution())