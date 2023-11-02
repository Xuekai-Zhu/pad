def solution():
    """A pack of pretzels costs $4, while a pack of chips is 75% more expensive. Maciek went and bought two packets of chips and two packets of pretzels. How much did he pay for his purchases?"""
    pretzel_price = 4
    chip_price = pretzel_price * 1.75
    total_cost = (2 * pretzel_price) + (2 * chip_price)
    result = total_cost
    return result

print(solution())