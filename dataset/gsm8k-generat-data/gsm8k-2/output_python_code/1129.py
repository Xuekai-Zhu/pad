def solution():
    """Max works for a delivery company as a courier. During one working day, he can deliver a maximum of 35 packages. One week, Max delivered the maximum number of packages, only twice. On two other days, Max unloaded a total of 50 packages, and on one day he unloaded only one-seventh of the maximum possible daily performance. On the last two days, the sum of the packages transported was only fourth-fifth of the maximum daily performance. How many more packages could Max deliver during that week, if he would work at maximum performance?"""
    max_daily_packages = 35
    max_delivered_days = 2
    unloaded_packages_days = 2
    unloaded_packages = 50
    one_seventh_max = max_daily_packages / 7
    fourth_fifth_max = max_daily_packages * 4 / 5

    total_packages_delivered = max_delivered_days * max_daily_packages + \
                               unloaded_packages_days * unloaded_packages + \
                               one_seventh_max + \
                               fourth_fifth_max * 2

    max_packages_deliverable = 7 * max_daily_packages

    result = max_packages_deliverable - total_packages_delivered
    return result

print(solution())