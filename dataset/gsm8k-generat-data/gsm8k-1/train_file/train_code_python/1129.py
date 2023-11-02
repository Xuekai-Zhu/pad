def solution():
    """Max works for a delivery company as a courier. During one working day, he can deliver a maximum of 35 packages. One week, Max delivered the maximum number of packages, only twice. On two other days, Max unloaded a total of 50 packages, and on one day he unloaded only one-seventh of the maximum possible daily performance. On the last two days, the sum of the packages transported was only fourth-fifth of the maximum daily performance. How many more packages could Max deliver during that week, if he would work at maximum performance?"""
    max_daily_performance = 35
    packages_delivered = 2 * max_daily_performance
    packages_unloaded = 50
    packages_unloaded_one_seventh = max_daily_performance / 7
    packages_transported = int(4/5 * max_daily_performance) * 2
    total_packages = packages_delivered + packages_unloaded + packages_unloaded_one_seventh + packages_transported
    max_possible_packages = max_daily_performance * 7
    result = max_possible_packages - total_packages
    return result

print(solution())