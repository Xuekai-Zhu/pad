def solution():
    # Define the price of the TV
    tv_price = 1700

    # Calculate the value added tax
    vat = 0.15 * tv_price

    # Calculate the price of the TV with VAT
    total_price = tv_price + vat
    result = total_price
    return result

print(solution())