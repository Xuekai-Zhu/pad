def solution():
    center1_packages_per_day = 10000
    center2_packages_per_day = center1_packages_per_day * 3
    profit_per_package = 0.05
    days_per_week = 7

    # Calculate the total number of packages processed per week by both centers
    total_packages_per_week = (center1_packages_per_day + center2_packages_per_day) * days_per_week

    # Calculate the total profit per week
    total_profit = total_packages_per_week * profit_per_package
    result = total_profit
    return result

print(solution())