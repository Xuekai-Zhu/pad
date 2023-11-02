def solution():
    bob_bill = 30
    kate_bill = 25

    # Calculate the discounts
    bob_discount = 0.05 * bob_bill
    kate_discount = 0.02 * kate_bill

    # Calculate the total amount after discounts
    total_bill = bob_bill + kate_bill - bob_discount - kate_discount
    result = total_bill
    return result

print(solution())