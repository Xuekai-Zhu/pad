def solution():
    """Angela is a bike messenger in New York. She needs to deliver 8 times as many packages as meals. If she needs to deliver 27 meals and packages combined, how many meals does she deliver?"""
    total_deliveries = 27
    packages = total_deliveries / 9
    meals = total_deliveries - packages
    result = meals
    return result

print(solution())