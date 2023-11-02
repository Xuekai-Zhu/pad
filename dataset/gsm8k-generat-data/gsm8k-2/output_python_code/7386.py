def solution():
    """Jose threatened to withhold 20% of Amanda's pay if she does not finish her sales report by midnight. 
    If Amanda makes $50.00 an hour and works for 10 hours a day, how much money will she receive if she does not finish the sales report by midnight?"""
    hourly_pay = 50
    hours_worked = 10
    total_earned = hourly_pay * hours_worked
    withholding_percent = 0.2
    withheld_amount = total_earned * withholding_percent
    amount_received = total_earned - withheld_amount
    result = amount_received
    return result

print(solution())