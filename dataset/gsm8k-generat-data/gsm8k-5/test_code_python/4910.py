def solution():
    total_devices = 50  # The school needs virus protection for 50 devices
    devices_per_package_a = 5  # The $40 package covers up to 5 devices
    devices_per_package_b = 10  # The $60 package covers up to 10 devices

    # Calculate the total number of packages needed for each type of software
    packages_a = total_devices // devices_per_package_a + int(total_devices % devices_per_package_a > 0)
    packages_b = total_devices // devices_per_package_b + int(total_devices % devices_per_package_b > 0)

    # Calculate the total cost of each type of software
    cost_a = packages_a * 40
    cost_b = packages_b * 60

    # Calculate the amount the school can save by buying the $60 software package
    savings = cost_a - cost_b
    result = savings
    return result

print(solution())