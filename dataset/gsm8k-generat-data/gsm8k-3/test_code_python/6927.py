def solution():
    """The Martin family goes to the mall to get ice cream.  A kiddie scoop is $3.  A regular scoop is $4.  A double scoop is $6.   Mr. and Mrs. Martin each get the regular scoop.  Their two children each get the kiddie scoop.  Their three teenage children each get double scoops.  How much money does Mrs. Martin pay the cashier?"""
    # Define the prices of each type of scoop
    KIDDIE_PRICE = 3
    REGULAR_PRICE = 4
    DOUBLE_PRICE = 6

    # Define the number of each type of scoop ordered
    kiddie_scoops = 2
    regular_scoops = 2
    double_scoops = 3 * 2

    # Calculate the total cost
    total_cost = (kiddie_scoops * KIDDIE_PRICE) + (regular_scoops * REGULAR_PRICE) + (double_scoops * DOUBLE_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())