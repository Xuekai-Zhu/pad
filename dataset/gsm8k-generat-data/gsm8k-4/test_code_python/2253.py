def solution():
    """Ines had $20 in her purse. She bought 3 pounds of peaches, which are $2 per pound at the local farmers’ market. How much did she have left?"""
    # Define the initial amount of money in Ines' purse
    initial_money = 20

    # Define the price of each pound of peaches
    peach_price = 2

    # Define the number of pounds of peaches bought
    peach_pounds = 3

    # Calculate the total cost of the peaches
    peach_cost = peach_price * peach_pounds

    # Calculate the remaining amount of money in Ines' purse
    remaining_money = initial_money - peach_cost

    # Return the result
    result = remaining_money
    return result

print(solution())