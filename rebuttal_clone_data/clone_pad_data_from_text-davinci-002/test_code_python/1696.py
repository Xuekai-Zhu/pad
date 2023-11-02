def solution():
    bill_total = 150
    tip_percent = 10
    tip_amount = bill_total * (tip_percent / 100)
    bill_minus_tip = bill_total + tip_amount
    silas_cost = bill_minus_tip / 2
    share_cost = bill_minus_tip - silas_cost
    result = share_cost / 5
    
    return result

print(solution())