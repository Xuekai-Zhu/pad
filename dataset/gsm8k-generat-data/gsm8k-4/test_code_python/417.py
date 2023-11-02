def solution():
    """Jim buys a package of 20 car washes. Since He bought a package he only has to pay 60%. A carwash normally costs 15 dollars. How much did he pay for the package?"""
    # Define the regular price of a car wash
    regular_price = 15

    # Define the number of car washes in the package
    num_washes = 20

    # Define the discount percentage for buying the package
    discount_percentage = 0.4

    # Calculate the total cost of the package after discount
    discounted_price = regular_price * discount_percentage
    total_cost = discounted_price * num_washes

    result = total_cost
    return result

print(solution())