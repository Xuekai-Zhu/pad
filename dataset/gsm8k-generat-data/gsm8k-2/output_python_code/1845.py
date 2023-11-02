def solution():
    """Bob and Kate went to a restaurant for dinner. After they were done eating the waitress gave a $30 bill to Bob and a $25 bill to Kate, but told them they were eligible for special discounts; 5% for Bob, 2% for Kate. Considering the discounts, how much do they have to pay in total?"""
    bob_bill = 30
    kate_bill = 25
    bob_discount = 0.05 * bob_bill
    kate_discount = 0.02 * kate_bill
    total_bill = (bob_bill - bob_discount) + (kate_bill - kate_discount)
    result = total_bill
    return result

print(solution())