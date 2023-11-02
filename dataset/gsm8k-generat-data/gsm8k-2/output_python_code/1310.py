def solution():
    """I bought a TV for $1700 excluding tax. What is the price of the television when calculating 15% of the value-added tax?"""
    tv_price = 1700
    tax_percent = 15
    tax_amount = tv_price * (tax_percent/100)
    total_price = tv_price + tax_amount
    result = total_price
    return result

print(solution())