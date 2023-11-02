def solution():
    total_deliveries = 27  # Angela needs to deliver a total of 27 meals and packages
    packages_to_meals_ratio = 8  # Angela needs to deliver 8 times as many packages as meals

    # Calculate the total number of packages Angela needs to deliver
    total_packages = total_deliveries / (packages_to_meals_ratio + 1)

    # Calculate the total number of meals Angela needs to deliver
    total_meals = total_packages / packages_to_meals_ratio

    result = total_meals
    return result

print(solution())