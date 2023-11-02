def solution():
    # Calculate the amount James sold the house for
    sale_price = 500000 * 1.2  # 20% over market value

    # Calculate the amount each person gets after taxes
    post_tax_amount = (sale_price / 4) * 0.9  # split revenue with 3 brothers and subtract 10% in taxes

    result = post_tax_amount
    return result

print(solution())