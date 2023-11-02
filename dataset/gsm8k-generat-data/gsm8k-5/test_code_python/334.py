def solution():
    # Calculate the cost of strawberries for 1 quart of strawberry ice cream
    cups_of_strawberries = 4  # Martha needs 4 cups of berries to make 1 quart of ice cream
    strawberries_per_package = 2  # Each package of strawberries contains 2 cups of berries
    packages_of_strawberries = cups_of_strawberries / strawberries_per_package
    cost_of_strawberries = packages_of_strawberries * 3.00

    # Calculate the cost of raspberries for 1 quart of raspberry ice cream
    cups_of_raspberries = 4  # Martha needs 4 cups of berries to make 1 quart of ice cream
    raspberries_per_package = 2  # Each package of raspberries contains 2 cups of berries
    packages_of_raspberries = cups_of_raspberries / raspberries_per_package
    cost_of_raspberries = packages_of_raspberries * 5.00

    # Calculate the cost of heavy cream for 2 quarts of ice cream
    cups_of_heavy_cream = 2  # Martha needs 2 cups of heavy cream to make 1 quart of ice cream
    container_of_heavy_cream = 4  # The heavy cream is sold in 4-cup containers
    containers_of_heavy_cream = cups_of_heavy_cream / container_of_heavy_cream
    cost_of_heavy_cream = containers_of_heavy_cream * 4.00

    # Calculate the total cost of making 2 quarts of ice cream
    total_cost = cost_of_strawberries + cost_of_raspberries + cost_of_heavy_cream
    result = total_cost
    return result

print(solution())