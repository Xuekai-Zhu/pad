def solution():
    packages_first_center = 10000
    packages_second_center = packages_first_center * 3
    total_packages = packages_first_center + packages_second_center
    profit_first_center = packages_first_center * 0.05
    profit_second_center = packages_second_center * 0.05
    total_profit = profit_first_center + profit_second_center
    result = total_profit
    return result

print(solution())