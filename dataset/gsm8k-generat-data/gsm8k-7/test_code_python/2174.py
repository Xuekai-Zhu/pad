def solution():
    original_price = 120
    discount = 0.5  # 50% discount
    reduced_price = original_price * (1 - discount)
    sales_tax = 0.05  # 5% sales tax
    total_cost = reduced_price * (1 + sales_tax)
    result = total_cost
    return result

print(solution())