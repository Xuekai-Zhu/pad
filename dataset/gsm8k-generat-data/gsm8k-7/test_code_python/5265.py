def solution():
    chocolates_per_dozen = 12
    minutes_per_package = 5
    hours_worked = 4

    # Calculate the total number of packages Wendy can make in 4 hours
    total_packages = (hours_worked * 60) / minutes_per_package

    # Calculate the total number of chocolates in all packages
    total_chocolates = total_packages * chocolates_per_dozen

    result = total_chocolates
    return result

print(solution())