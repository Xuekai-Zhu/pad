def solution():
    # Define the original bills
    bob_bill = 30
    kate_bill = 25

    # Calculate the discounts
    bob_discount = bob_bill * 0.05
    kate_discount = kate_bill * 0.02

    # Calculate the new bills after the discounts
    bob_new_bill = bob_bill - bob_discount
    kate_new_bill = kate_bill - kate_discount

    # Calculate the total amount to pay
    total_pay = bob_new_bill + kate_new_bill
    result = total_pay
    return result

print(solution())