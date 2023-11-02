def solution():
    """Jim buys a package of 20 car washes.  Since He bought a package he only has to pay 60%.  A carwash normally costs 15 dollars.  How much did he pay for the package?"""
    # Define the regular price and discount percentage
    REGULAR_PRICE = 15
    DISCOUNT_PERCENTAGE = 0.6

    # Define the number of car washes in the package
    PACKAGE_SIZE = 20

    # Calculate the discounted price of a single car wash
    discounted_price = REGULAR_PRICE * DISCOUNT_PERCENTAGE

    # Calculate the total cost of the package
    package_cost = discounted_price * PACKAGE_SIZE

    # Display the total cost
    result = package_cost
    return result

print(solution())