def solution():
    """A school is buying virus protection software to cover 50 devices.  One software package costs $40 and covers up to 5 devices. The other software package costs $60 and covers up to 10 devices.  How much money, in dollars, can the school save by buying the $60 software package instead of the $40 software package?"""
    # Define the number of devices to be covered and the cost of each package
    num_devices = 50
    package1_cost = 40
    package1_num_devices = 5
    package2_cost = 60
    package2_num_devices = 10

    # Calculate the number of each package needed to cover all devices
    num_package1 = (num_devices - 1) // package1_num_devices + 1
    num_package2 = (num_devices - 1) // package2_num_devices + 1

    # Calculate the total cost of each package based on the number needed
    total_cost1 = num_package1 * package1_cost
    total_cost2 = num_package2 * package2_cost

    # Calculate the amount saved by buying the $60 software package instead of the $40 software package
    savings = total_cost1 - total_cost2

    # Display the amount saved
    result = savings
    return result

print(solution())