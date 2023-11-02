def solution():
    bill1 = 200
    bill2 = 130
    bill3 = 444
    interest_bill1 = bill1 * 0.1
    total_bill1 = interest_bill1 + bill1
    late_fee_bill2 = bill2 * 0.5
    total_bill2 = late_fee_bill2 + bill2
    late_fee_bill3 = 40
    total_bill3 = late_fee_bill3 + bill3
    total_amount_owed = total_bill1 + total_bill2 + total_bill3
    
    return total_amount_owed

print(solution())