def solution():
    """Max works for a delivery company as a courier. During one working day, he can deliver a maximum of 35 packages. One week, Max delivered the maximum number of packages, only twice. On two other days, Max unloaded a total of 50 packages, and on one day he unloaded only one-seventh of the maximum possible daily performance. On the last two days, the sum of the packages transported was only fourth-fifth of the maximum daily performance. How many more packages could Max deliver during that week, if he would work at maximum performance?"""
    # Define the maximum number of packages Max can deliver in a day
    MAX_PACKAGES = 35

    # Calculate the total number of packages Max delivered on the two days at maximum performance
    max_days_delivered = 2 * MAX_PACKAGES

    # Calculate the total number of packages Max unloaded on the two other days
    total_unloaded_packages = 50

    # Calculate the number of packages Max unloaded on the day he performed at 1/7 of his maximum performance
    unloaded_one_seventh = MAX_PACKAGES / 7

    # Calculate the total number of packages Max transported on the last two days
    total_transport_packages = (4/5) * MAX_PACKAGES * 2

    # Calculate the total number of packages Max could have delivered if he had worked at maximum performance
    max_possible_packages = max_days_delivered + MAX_PACKAGES + total_unloaded_packages + (unloaded_one_seventh * 5) + total_transport_packages

    # Calculate the number of additional packages Max could have delivered
    additional_packages = max_possible_packages - (MAX_PACKAGES * 7)

    result = additional_packages
    return result

print(solution())