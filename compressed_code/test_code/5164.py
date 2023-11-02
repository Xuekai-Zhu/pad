def solution():
    
    bill_amount = 20
    sodas_bought = 3
    total_change = 14
    total_spent = bill_amount - total_change
    soda_cost = total_spent / sodas_bought
    result = soda_cost
    return result

print(solution())