def solution():
    
    bob_bill = 30
    kate_bill = 25
    bob_discount = bob_bill * 0.05
    kate_discount = kate_bill * 0.02
    total_bill = bob_bill - bob_discount + kate_bill - kate_discount
    result = total_bill
    return result

print(solution())