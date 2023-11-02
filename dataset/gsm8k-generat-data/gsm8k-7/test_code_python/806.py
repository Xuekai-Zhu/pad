def solution():
    original_price = 200
    discount = 0.25  # 25% discount
    discounted_price = original_price * (1 - discount)
    sales_tax = 0.1  # 10% sales tax
    total_cost = discounted_price * (1 + sales_tax)
    result = total_cost
    return result

print(solution())