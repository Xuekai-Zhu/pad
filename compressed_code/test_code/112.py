def solution():
    
    total_deliveries = 27
    num_packages = 8
    num_meals = 1
    combined_packages_meals = num_packages + num_meals
    num_packages_delivered = total_deliveries / combined_packages_meals * num_packages
    num_meals_delivered = total_deliveries / combined_packages_meals * num_meals
    result = num_meals_delivered
    return result

print(solution())