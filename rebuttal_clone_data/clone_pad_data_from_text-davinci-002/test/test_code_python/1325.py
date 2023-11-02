def solution():
    total_charge = 74 + (2 * 2) + 42
    discount_amount = total_charge - 100
    total_discount = discount_amount * 0.1
    final_charge = total_charge - total_discount
    result = final_charge
    return result

print(solution())