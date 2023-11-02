def solution():
    """Mark buys a loaf of bread for $4.20 and some cheese for $2.05. He gives the cashier $7.00. If the cashier only has 1 quarter and 1 dime in his till, plus a bunch of nickels, how many nickels does Mark get in his change?"""
    total_cost = 4.20 + 2.05
    amount_paid = 7.00
    change = amount_paid - total_cost
    num_quarters = 1
    num_dimes = 1
    value_of_quarters = num_quarters * 0.25
    value_of_dimes = num_dimes * 0.10
    value_of_nickels = change - value_of_quarters - value_of_dimes
    num_nickels = int(value_of_nickels / 0.05)
    result = num_nickels
    return result

print(solution())