def solution():
    """At Clark's Food Store, apples cost 40 dollars for a dozen, and pears cost 50 dollars for a dozen. If Hank bought 14 dozen of each kind of fruit, how many dollars did he spend?"""
    # Define the price of a dozen apples and a dozen pears
    APPLE_PRICE = 40
    PEAR_PRICE = 50

    # Define the number of dozens of each fruit purchased
    apple_dozens = 14
    pear_dozens = 14

    # Calculate the total cost of the apples
    apple_cost = apple_dozens * APPLE_PRICE

    # Calculate the total cost of the pears
    pear_cost = pear_dozens * PEAR_PRICE

    # Calculate the total cost of all the fruit
    total_cost = apple_cost + pear_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())