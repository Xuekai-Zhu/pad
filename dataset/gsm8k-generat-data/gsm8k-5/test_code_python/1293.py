def solution():
    jimmy_total = 3 * 15  # Jimmy's total amount before the discount
    irene_total = 5 * 17  # Irene's total amount before the discount
    total_before_discount = jimmy_total + irene_total  # Total amount before the discount

    # Applying the senior citizen discount
    total_after_discount = total_before_discount * 0.9

    result = total_after_discount
    return result

print(solution())