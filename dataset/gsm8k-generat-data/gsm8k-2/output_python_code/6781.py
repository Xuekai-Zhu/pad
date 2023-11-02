def solution():
    """Hendricks buys a guitar for $200, which is 20% less than what Gerald bought the same guitar for. How much did Gerald pay for his guitar?"""
    hendricks_price = 200
    discount = 0.2
    gerald_price = hendricks_price / (1 - discount)
    result = gerald_price
    return result

print(solution())