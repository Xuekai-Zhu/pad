def solution():
    tv_price = 1700
    tax_rate = 0.15  # 15% tax rate

    # Calculate the amount of tax
    tax_amount = tv_price * tax_rate

    # Calculate the total price including tax
    total_price = tv_price + tax_amount
    result = total_price
    return result

print(solution())