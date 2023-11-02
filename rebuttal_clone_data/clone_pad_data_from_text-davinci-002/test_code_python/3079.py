def solution():
    sales_tax = 0.095
    original_cost = (14.50 / (1 - 0.5)) * (1 + sales_tax)
    result = original_cost
    return result

print(solution())