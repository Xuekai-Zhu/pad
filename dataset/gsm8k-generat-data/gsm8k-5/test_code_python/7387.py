def solution():
    hourly_pay = 50.00  # Amanda makes $50.00 an hour
    hours_worked = 10  # Amanda works for 10 hours a day
    total_pay = hourly_pay * hours_worked  # Amanda's total pay for the day before the deadline

    withheld_amount = 0.2 * total_pay  # Jose threatened to withhold 20% of Amanda's pay

    if withheld_amount == total_pay:
        result = 0  # Amanda will receive no money if she does not finish the report
    else:
        result = total_pay - withheld_amount  # Amanda's pay after the withholding
    return result

print(solution())