def solution():
    """A 220-liter barrel has a small leak. It lost 10% of its contents before anyone noticed. How many liters are left in the barrel?"""
    barrel_size = 220
    leak_percentage = 0.1
    remaining_percentage = 1 - leak_percentage
    remaining_liters = remaining_percentage * barrel_size
    result = remaining_liters
    return result

print(solution())