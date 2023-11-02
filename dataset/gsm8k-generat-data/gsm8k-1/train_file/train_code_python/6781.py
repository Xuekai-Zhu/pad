def solution():
    """Hendricks buys a guitar for $200, which is 20% less than what Gerald bought the same guitar for. How much did Gerald pay for his guitar?"""
    hendricks_price = 200
    percent_off = 20
    original_price = hendricks_price / (1 - percent_off/100)
    result = original_price
    return result

print(solution())