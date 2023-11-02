def solution():
    # Determine how many cups of berries Martin will need for 30 days
    cups_per_day = 1/2
    cups_for_30_days = cups_per_day * 30

    # Determine how many packages of berries Martin will need to buy
    berries_per_package = 1
    packages_needed = cups_for_30_days / berries_per_package

    # Calculate the total cost of buying the needed packages
    cost_per_package = 2.0
    total_cost = packages_needed * cost_per_package

    result = total_cost
    return result

print(solution())