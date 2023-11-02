def solution():
    """I bought a TV for $1700 excluding tax. What is the price of the television when calculating 15% of the value-added tax?"""
    # Define the price of the TV
    tv_price = 1700

    # Calculate the value of the 15% tax
    tax_value = 0.15 * tv_price

    # Calculate the total price of the TV with tax
    total_price = tv_price + tax_value

    result = total_price
    return result

print(solution())