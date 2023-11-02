def solution():
    """Mark buys a loaf of bread for $4.20 and some cheese for $2.05. He gives the cashier $7.00. If the cashier only has 1 quarter and 1 dime in his till, plus a bunch of nickels, how many nickels does Mark get in his change?"""
    # Calculate the total cost of the items purchased
    total_cost = 4.20 + 2.05

    # Calculate the amount of change Mark should receive
    change = 7.00 - total_cost

    # Calculate the number of nickels in Mark's change
    nickels = int((change - 0.25 - 0.1) / 0.05)

    # Display the number of nickels
    result = nickels
    return result

print(solution())