def solution():
    
    packages_center1 = 10000
    packages_center2 = 3 * packages_center1
    total_packages = packages_center1 + packages_center2
    profit_per_package = 0.05
    total_profit = total_packages * profit_per_package * 7
    
    return total_profit

print(solution())