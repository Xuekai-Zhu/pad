def solution():
    bob_bill = 30
    kate_bill = 25

    bob_discount = 0.05  # 5% discount
    kate_discount = 0.02  # 2% discount

    # Calculate the amount of discount for Bob
    bob_discount_amount = bob_bill * bob_discount

    # Calculate the amount of discount for Kate
    kate_discount_amount = kate_bill * kate_discount

    # Calculate the total bill for Bob and Kate after discounts
    total_bill = bob_bill - bob_discount_amount + kate_bill - kate_discount_amount
    result = total_bill
    return result

print(solution())