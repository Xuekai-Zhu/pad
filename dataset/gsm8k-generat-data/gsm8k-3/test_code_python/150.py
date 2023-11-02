def solution():
    """Angela is a bike messenger in New York. She needs to deliver 8 times as many packages as meals. If she needs to deliver 27 meals and packages combined, how many meals does she deliver?"""
    # Define the total number of packages as a multiple of meals
    package_multiple = 8

    # Calculate the total number of packages
    total_packages = package_multiple * 27

    # Calculate the total number of meals and packages combined
    total_deliveries = total_packages + 27

    # Calculate the number of meals delivered
    meals_delivered = 27

    # Subtract the number of meals delivered from the total to get the number of packages delivered
    packages_delivered = total_deliveries - meals_delivered

    # Divide the number of packages by the multiple to get the number of meals delivered
    meals_delivered = packages_delivered / package_multiple

    # Return the result
    result = meals_delivered
    return result

print(solution())