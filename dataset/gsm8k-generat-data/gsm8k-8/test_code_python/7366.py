def solution():
    # Define the number of packages received yesterday and today
    yesterday_packages = 80
    today_packages = 2 * yesterday_packages

    # Calculate the total number of packages
    total_packages = yesterday_packages + today_packages

    # The number of packages to be delivered tomorrow is the same as the total number of packages
    result = total_packages
    return result

print(solution())