def solution():
    packages_yesterday = 80  # The courier received 80 packages yesterday
    packages_today = 2 * packages_yesterday  # The courier received twice as many packages today
    total_packages = packages_yesterday + packages_today  # The total number of packages to be delivered tomorrow

    result = total_packages
    return result

print(solution())