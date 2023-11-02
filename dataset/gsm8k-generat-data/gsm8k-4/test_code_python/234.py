def solution():
    """Mark buys a loaf of bread for $4.20 and some cheese for $2.05. He gives the cashier $7.00. If the cashier only has 1 quarter and 1 dime in his till, plus a bunch of nickels, how many nickels does Mark get in his change?"""
    # Define the cost of the bread and cheese, and the amount paid by Mark
    bread_cost = 4.20
    cheese_cost = 2.05
    total_paid = 7.00

    # Calculate the total cost of the purchase
    total_cost = bread_cost + cheese_cost

    # Calculate the amount of change owed to Mark
    change = total_paid - total_cost

    # Calculate the number of nickels in the change
    nickel_count = 0
    while change > 0.05:
        change -= 0.05
        nickel_count += 1

    # Return the result - the number of nickels in the change
    result = nickel_count
    return result

print(solution())