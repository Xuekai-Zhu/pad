def solution():
    """A porcelain vase was originally priced at $200 but went on sale for 25% off. If Donna bought the porcelain vase and paid 10% sales tax, how much did she pay in total?"""
    original_price = 200
    sale_price = original_price * 0.75
    tax_rate = 0.1
    total_price = sale_price * (1 + tax_rate)
    result = total_price
    return result

print(solution())