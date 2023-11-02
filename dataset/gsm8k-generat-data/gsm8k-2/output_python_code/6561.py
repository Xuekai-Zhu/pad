def solution():
    """A pack of pretzels costs $4, while a pack of chips is 75% more expensive. Maciek went and bought two packets of chips and two packets of pretzels. How much did he pay for his purchases?"""
    pretzel_cost = 4
    chip_cost = 1.75 * pretzel_cost
    total_cost = (2 * pretzel_cost) + (2 * chip_cost)
    result = total_cost
    return result

print(solution())