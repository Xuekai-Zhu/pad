def solution():
    original_price = 200  # Original price of the vase is $200
    discount = 0.25  # The vase is on sale for 25% off
    sale_price = original_price * (1 - discount)  # Calculate the sale price

    sales_tax_rate = 0.1  # Sales tax is 10%
    total_price = sale_price * (1 + sales_tax_rate)  # Calculate the total price

    result = total_price
    return result

print(solution())