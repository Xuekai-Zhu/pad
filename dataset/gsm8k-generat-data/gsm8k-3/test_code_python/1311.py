def solution():
    """I bought a TV for $1700 excluding tax. What is the price of the television when calculating 15% of the value-added tax?"""
    # Define the price of the TV
    price = 1700

    # Calculate the value-added tax
    vat = price * 0.15

    # Calculate the total price including VAT
    total_price = price + vat

    # Display the total price
    result = total_price
    return result

print(solution())