def solution():
    # Calculate the total maximum packages Max could deliver in a week
    max_weekly_packages = 35 * 7 * 2

    # Calculate the total packages Max unloaded on the two days
    unloaded_packages = 50

    # Calculate the packages Max unloaded on the day he performed at one-seventh of his maximum
    unloaded_one_seventh = int(35 / 7)

    # Calculate the packages Max transported on the last two days
    transported_last_two_days = int((35 * 4 / 5) * 2)

    # Calculate the total packages Max could deliver if he worked at maximum performance every day
    total_max_weekly_packages = max_weekly_packages + unloaded_packages - unloaded_one_seventh + transported_last_two_days

    # Calculate how many more packages Max could deliver if he worked at maximum performance every day
    more_packages = total_max_weekly_packages - max_weekly_packages
    result = more_packages
    return result

print(solution())