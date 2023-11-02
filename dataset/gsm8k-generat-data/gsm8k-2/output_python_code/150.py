def solution():
    """Angela is a bike messenger in New York. She needs to deliver 8 times as many packages as meals. If she needs to deliver 27 meals and packages combined, how many meals does she deliver?"""
    total_deliveries = 27
    num_packages = 8
    num_meals = 1
    combined_packages_meals = num_packages + num_meals
    num_packages_delivered = total_deliveries / combined_packages_meals * num_packages
    num_meals_delivered = total_deliveries / combined_packages_meals * num_meals
    result = num_meals_delivered
    return result

print(solution())