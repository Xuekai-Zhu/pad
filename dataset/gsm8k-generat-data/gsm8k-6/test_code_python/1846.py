def solution():
    # Calculate the amount of money Bob and Kate have to pay after the discounts
    bob_discount = 0.05 * 30  # 5% discount on $30 bill for Bob
    kate_discount = 0.02 * 25  # 2% discount on $25 bill for Kate
    total_bill = (30 - bob_discount) + (25 - kate_discount)  # calculate the total bill
    result = total_bill
    return result

print(solution())