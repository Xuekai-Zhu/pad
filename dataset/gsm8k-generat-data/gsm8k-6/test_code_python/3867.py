def solution():
    # Calculate the total number of workdays in 2 weeks
    total_workdays = 2 * 5  # she works 5 days a week for 2 weeks

    # Calculate the total paid vacation days
    total_paid_vacation = 6

    # Calculate the total unpaid vacation days
    total_unpaid_vacation = total_workdays - total_paid_vacation

    # Calculate the total amount of pay she will miss on unpaid vacation
    unpaid_vacation_pay = 15 * 8 * total_unpaid_vacation  # she works 8 hours a day at $15 per hour

    result = unpaid_vacation_pay
    return result

print(solution())