def solution():
    """Max works for a delivery company as a courier. During one working day, he can deliver a maximum of 35 packages. One week, Max delivered the maximum number of packages, only twice. On two other days, Max unloaded a total of 50 packages, and on one day he unloaded only one-seventh of the maximum possible daily performance. On the last two days, the sum of the packages transported was only fourth-fifth of the maximum daily performance. How many more packages could Max deliver during that week, if he would work at maximum performance?"""
    # Define the maximum number of packages Max can deliver in a day
    MAX_PACKAGES_PER_DAY = 35

    # Calculate the number of packages Max delivered at maximum performance
    max_delivery_days = 2
    max_delivery_packages = max_delivery_days * MAX_PACKAGES_PER_DAY

    # Calculate the number of packages Max unloaded on two other days
    unloaded_packages = 50

    # Calculate the number of packages Max unloaded on one day at one-seventh of the maximum daily performance
    unloaded_one_seventh = MAX_PACKAGES_PER_DAY / 7

    # Calculate the number of packages Max transported on the last two days at fourth-fifth of the maximum daily performance
    transported_four_fifth = 2 * MAX_PACKAGES_PER_DAY * 4 / 5

    # Calculate the total number of packages Max could have delivered at maximum performance
    total_packages = max_delivery_packages + unloaded_packages + unloaded_one_seventh + transported_four_fifth

    # Calculate the number of packages Max could deliver if he worked at maximum performance for the entire week
    max_packages = 7 * MAX_PACKAGES_PER_DAY

    # Calculate the difference between the total packages and the maximum packages Max could deliver
    extra_packages = max_packages - total_packages

    # Display the number of extra packages Max could deliver
    result = extra_packages
    return result

print(solution())