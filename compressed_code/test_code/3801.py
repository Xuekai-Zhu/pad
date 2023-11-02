def solution():
    
    devices = 50
    package_1_cost = 40
    package_1_devices = 5
    package_2_cost = 60
    package_2_devices = 10
    total_package_1_cost = devices//package_1_devices * package_1_cost + (devices % package_1_devices)*8
    total_package_2_cost = devices//package_2_devices * package_2_cost + (devices % package_2_devices)*6
    savings = total_package_1_cost - total_package_2_cost
    result = savings
    return result

print(solution())