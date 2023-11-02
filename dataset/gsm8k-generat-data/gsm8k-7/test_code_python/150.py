def solution():
    num_packages = 8
    num_meals = 1
    total_deliveries = 27

    # Calculate the total number of packages
    total_packages = total_deliveries / (num_packages + num_meals) * num_packages

    # Calculate the total number of meals
    total_meals = total_deliveries - total_packages

    result = total_meals
    return result

print(solution())