def solution():
    original_price = 120
    marked_down_price = 0.5 * original_price  # 50% discount
    additional_sales_tax = 0.05 * marked_down_price
    total_cost = marked_down_price + additional_sales_tax
    result = total_cost
    return result

print(solution())