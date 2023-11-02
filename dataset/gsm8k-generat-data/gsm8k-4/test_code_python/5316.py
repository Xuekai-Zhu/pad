def solution():
    """Shane prepares sandwiches for the Boy Scouts. He buys 2 packages of sliced bread containing 20 slices each, and he also buys 2 packages of sliced ham containing 8 slices each. Shane will make as many sandwiches as he can according to the ham he has. How many slices of bread will he have leftover?"""
    # Define the number of packages of bread and ham
    bread_packages = 2
    ham_packages = 2

    # Define the number of slices per package of bread and ham
    bread_slices_per_package = 20
    ham_slices_per_package = 8

    # Calculate the total number of slices of bread and ham
    total_bread_slices = bread_packages * bread_slices_per_package
    total_ham_slices = ham_packages * ham_slices_per_package

    # Calculate the maximum number of sandwiches that can be made based on the ham slices
    max_sandwiches = total_ham_slices // 2

    # Calculate the number of slices of bread leftover after making the maximum number of sandwiches
    leftover_bread_slices = total_bread_slices - (max_sandwiches * 2)

    # return the result
    result = leftover_bread_slices
    return result

print(solution())