def solution():
    cost_per_phone = 800
    discount = 5
    total_cost = 2 * cost_per_phone
    discount_amount = total_cost * (discount / 100)
    final_cost = total_cost - discount_amount
    result = final_cost
    return result

print(solution())