def solution():
    monthly_bill = 60
    percent_increase = 30
    increase_amount = monthly_bill * (percent_increase / 100)
    total_bill = monthly_bill + increase_amount
    result = total_bill
    return result

print(solution())