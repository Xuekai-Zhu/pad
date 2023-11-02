def solution():
    
    num_devices = 50
    package_1_price = 40
    package_1_coverage = 5
    package_2_price = 60
    package_2_coverage = 10
    
    
    num_package_1 = num_devices / package_1_coverage
    num_package_2 = num_devices / package_2_coverage
    
    
    total_cost_package_1 = num_package_1 * package_1_price
    total_cost_package_2 = num_package_2 * package_2_price
    
    
    cost_difference = total_cost_package_1 - total_cost_package_2
    
    return cost_difference

print(solution())