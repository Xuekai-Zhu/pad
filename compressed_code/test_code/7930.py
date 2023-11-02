def solution():
    
    initial_bill = 60
    percent_increase = 30
    increase_amount = initial_bill * (percent_increase / 100)
    total_bill = initial_bill + increase_amount
    result = total_bill
    return result

print(solution())