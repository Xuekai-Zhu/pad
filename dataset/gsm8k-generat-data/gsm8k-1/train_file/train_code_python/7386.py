def solution():
    """Jose threatened to withhold 20% of Amanda's pay if she does not finish her sales report by midnight. If Amanda makes $50.00 an hour and works for 10 hours a day, how much money will she receive if she does not finish the sales report by midnight?"""
    hourly_pay = 50.00
    hours_worked = 10
    total_earnings = hourly_pay * hours_worked
    percent_withheld = 20
    amount_withheld = total_earnings * (percent_withheld / 100)
    earnings_after_withhold = total_earnings - amount_withheld
    result = earnings_after_withhold
    return result

print(solution())