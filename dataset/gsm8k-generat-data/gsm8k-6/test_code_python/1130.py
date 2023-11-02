def solution():
    max_delivered = 35 * 2  # Max delivered the maximum number of packages only twice
    unloaded = 50  # On two other days, Max unloaded a total of 50 packages
    unloaded += 35//7  # On one day he unloaded only one-seventh of the maximum possible daily performance
    transported = 35 * (4/5) * 2  # On the last two days, the sum of the packages transported was only fourth-fifth of the maximum daily performance
    total_packages = max_delivered + unloaded + transported
    remaining_packages = (7 * 35) - total_packages
    result = remaining_packages
    return result

print(solution())