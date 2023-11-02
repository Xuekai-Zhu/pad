def solution():
    price_excluding_tax = 1700  # The TV costs $1700 excluding tax
    tax_percentage = 0.15  # The value-added tax is 15% of the price excluding tax

    # Calculate the price of the television with tax included
    price_with_tax = price_excluding_tax + (price_excluding_tax * tax_percentage)

    result = price_with_tax
    return result

print(solution())