def solution():
    """Martin eats 1/2 cup of berries every day.  The grocery store is selling a package of berries (1 cup per pack) for $2.00.  How much will he spend on berries in a 30 day period?"""
    # Define the amount of berries Martin eats per day
    BERRIES_PER_DAY = 0.5 # in cups

    # Calculate the number of berry packages needed for 30 days
    packages_needed = 30 * BERRIES_PER_DAY # in cups

    # Calculate the total cost of the required number of packages
    package_cost = 2.00
    total_cost = package_cost * packages_needed

    # Display the total cost
    result = total_cost
    return result

print(solution())