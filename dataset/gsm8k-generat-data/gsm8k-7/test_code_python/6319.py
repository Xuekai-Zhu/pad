def solution():
    num_pants = 10
    original_price = 45
    discount = 0.2  # 20% off
    sale_price = original_price * (1 - discount)
    tax_rate = 0.1  # 10% tax
    total_before_tax = num_pants * sale_price
    total_with_tax = total_before_tax * (1 + tax_rate)
    result = total_with_tax
    return result

print(solution())