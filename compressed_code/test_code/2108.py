def solution():
    
    base_bill = 60
    increase_percent = 30
    increase_amount = base_bill * (increase_percent / 100)
    total_bill = base_bill + increase_amount
    result = total_bill
    return result

print(solution())