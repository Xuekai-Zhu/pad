def solution():
    bill_amount = 150
    num_friends = 6
    silas_contribution = bill_amount / 2
    remaining_bill = bill_amount - silas_contribution
    tip_amount = remaining_bill * 0.1
    total_paid = remaining_bill + tip_amount
    amount_per_person = total_paid / (num_friends - 1)
    result = amount_per_person
    return result

print(solution())