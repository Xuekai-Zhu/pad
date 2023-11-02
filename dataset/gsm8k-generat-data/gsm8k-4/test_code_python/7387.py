def solution():
    """Jose threatened to withhold 20% of Amanda's pay if she does not finish her sales report by midnight. If Amanda makes $50.00 an hour and works for 10 hours a day, how much money will she receive if she does not finish the sales report by midnight?"""
    # Define Amanda's hourly rate and number of hours worked
    hourly_rate = 50.00
    hours_worked = 10

    # Calculate Amanda's gross pay for the day
    gross_pay = hourly_rate * hours_worked

    # Calculate the amount that will be withheld if she does not finish her sales report
    withholding_amount = gross_pay * 0.2

    # Calculate Amanda's net pay after withholding
    net_pay = gross_pay - withholding_amount

    result = net_pay
    return result

print(solution())