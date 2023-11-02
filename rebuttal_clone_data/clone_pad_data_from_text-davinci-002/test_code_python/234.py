def solution():
    """Mark buys a loaf of bread for $4.20 and some cheese for $2.05. He gives the cashier $7.00. If the cashier only has 1 quarter and 1 dime in his till, plus a bunch of nickels, how many nickels does Mark get in his change?"""
    cost_of_bread = 4.2
    cost_of_cheese = 2.05
    money_given = 7.0
    money_owed = cost_of_bread + cost_of_cheese
    change_due = money_given - money_owed
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    num_quarters = 1
    num_dimes = 1
    num_nickels = (change_due - (quarter * num_quarters) - (dime * num_dimes)) / nickel
    result = num_nickels
    return result

print(solution())