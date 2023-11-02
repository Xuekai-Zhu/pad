def solution():
    monthly_bill = 50
    percent_increase = 10
    increase_amount = monthly_bill * (percent_increase / 100)
    new_monthly_bill = monthly_bill + increase_amount
    one_year_bill = new_monthly_bill * 12
    result = one_year_bill
    
    return result

print(solution())