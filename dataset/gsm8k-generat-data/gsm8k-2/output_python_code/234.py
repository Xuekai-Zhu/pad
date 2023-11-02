def solution():
    """Mark buys a loaf of bread for $4.20 and some cheese for $2.05. He gives the cashier $7.00. If the cashier only has 1 quarter and 1 dime in his till, plus a bunch of nickels, how many nickels does Mark get in his change?"""
    total_cost = 4.20 + 2.05
    payment = 7.00
    change = payment - total_cost
    nickels = int((change - 0.25 - 0.10) / 0.05)
    result = nickels
    return result

print(solution())