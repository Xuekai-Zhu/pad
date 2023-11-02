def solution():
    cost_of_candy = 0.44
    payment = 1.0

    # Calculate the amount of change that Rosie will get
    change = payment - cost_of_candy

    # Calculate the number of coins that Rosie will get as change
    num_quarters = int(change / 0.25)
    change = change - (num_quarters * 0.25)

    num_dimes = int(change / 0.10)
    change = change - (num_dimes * 0.10)

    num_nickels = int(change / 0.05)
    change = change - (num_nickels * 0.05)

    num_pennies = int(round(change / 0.01))

    total_coins = num_quarters + num_dimes + num_nickels + num_pennies
    result = total_coins
    return result

print(solution())