def solution():
    """Ines had $20 in her purse. She bought 3 pounds of peaches, which are $2 per pound at the local farmers’ market. How much did she have left?"""
    # Define the cost of a pound of peaches
    peach_price = 2

    # Define the number of pounds of peaches bought
    peach_pounds = 3

    # Calculate the total cost of the peaches
    total_cost = peach_price * peach_pounds

    # Subtract the total cost from the initial amount of money
    money_left = 20 - total_cost

    # Display the remaining amount of money
    result = money_left
    return result

print(solution())