def solution():
    # Calculate Amanda's salary before the threat of withholding pay
    hourly_rate = 50.00
    hours_worked = 10
    pre_threat_salary = hourly_rate * hours_worked

    # Calculate how much Amanda will get if she does not finish the sales report by midnight
    withholding_percentage = 0.20
    amount_withheld = withholding_percentage * pre_threat_salary
    post_threat_salary = pre_threat_salary - amount_withheld
    result = post_threat_salary
    return result

print(solution())