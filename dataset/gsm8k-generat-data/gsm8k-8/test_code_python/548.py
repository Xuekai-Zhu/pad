def solution():
    # Define the number of packages processed by each center per day
    center1_packages = 10000
    center2_packages = 3 * center1_packages

    # Calculate the total number of packages processed per week
    total_packages_per_week = 7 * (center1_packages + center2_packages)

    # Calculate the total profit per week
    profit_per_package = 0.05
    total_profit_per_week = total_packages_per_week * profit_per_package

    result = total_profit_per_week
    return result

print(solution())