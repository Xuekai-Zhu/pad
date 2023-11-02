def solution():
    """A school is buying virus protection software to cover 50 devices. One software package costs $40 and covers up to 5 devices. The other software package costs $60 and covers up to 10 devices. How much money, in dollars, can the school save by buying the $60 software package instead of the $40 software package?"""
    num_devices = 50
    package_1_price = 40
    package_1_coverage = 5
    package_2_price = 60
    package_2_coverage = 10
    
    # Calculate number of each type of package needed
    num_package_1 = num_devices / package_1_coverage
    num_package_2 = num_devices / package_2_coverage
    
    # Calculate total cost for each package
    total_cost_package_1 = num_package_1 * package_1_price
    total_cost_package_2 = num_package_2 * package_2_price
    
    # Calculate difference in cost
    cost_difference = total_cost_package_1 - total_cost_package_2
    
    return cost_difference

print(solution())