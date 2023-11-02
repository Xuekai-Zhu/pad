def solution():
    
    bob_bill = 30
    kate_bill = 25
    bob_discount = 0.05 * bob_bill
    kate_discount = 0.02 * kate_bill
    total_bill = (bob_bill - bob_discount) + (kate_bill - kate_discount)
    result = total_bill
    return result

print(solution())