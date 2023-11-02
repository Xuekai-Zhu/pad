def solution():
    """A school is buying virus protection software to cover 50 devices. One software package costs $40 and covers up to 5 devices.
    The other software package costs $60 and covers up to 10 devices. How much money, in dollars, can the school save by buying the $60 software package instead of the $40 software package?"""
    # Define the number of devices and the prices of the software packages
    devices = 50
    package_1_price = 40
    package_1_devices = 5
    package_2_price = 60
    package_2_devices = 10

    # Calculate the cost of buying package 1
    packages_needed_1 = devices // package_1_devices
    remainder_devices_1 = devices % package_1_devices
    if remainder_devices_1 > 0:
        packages_needed_1 += 1
    cost_1 = packages_needed_1 * package_1_price

    # Calculate the cost of buying package 2
    packages_needed_2 = devices // package_2_devices
    remainder_devices_2 = devices % package_2_devices
    if remainder_devices_2 > 0:
        packages_needed_2 += 1
    cost_2 = packages_needed_2 * package_2_price

    # Calculate the savings
    savings = cost_1 - cost_2

    # return the result
    result = savings
    return result

print(solution())