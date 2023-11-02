def solution():
    cost_before_tax = 40
    tax_rate = 0.05
    discount = 8
    cost_after_tax = cost_before_tax + cost_before_tax*tax_rate - discount
    final_price = cost_after_tax/2
    result = final_price
    return result

print(solution())