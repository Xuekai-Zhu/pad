def solution():
    
    bill_amount = 50
    tip_percent = 20
    tip_amount = bill_amount * (tip_percent / 100)
    total_amount = bill_amount + tip_amount
    result = total_amount
    return result

print(solution())