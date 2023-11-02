def solution():
    """A school is buying virus protection software to cover 50 devices. One software package costs $40 and covers up to 5 devices. The other software package costs $60 and covers up to 10 devices. How much money, in dollars, can the school save by buying the $60 software package instead of the $40 software package?"""
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