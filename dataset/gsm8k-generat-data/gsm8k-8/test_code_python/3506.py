def solution():
    # Define the value of the candy and bill
    candy_cost = 0.44
    bill_value = 1

    # Calculate the total amount of change
    total_change = bill_value - candy_cost

    # Define the values of each type of coin
    quarter_value = 0.25
    dime_value = 0.1
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the number of each type of coin
    num_quarters = int(total_change / quarter_value)
    total_change -= num_quarters * quarter_value

    num_dimes = int(total_change / dime_value)
    total_change -= num_dimes * dime_value

    num_nickels = int(total_change / nickel_value)
    total_change -= num_nickels * nickel_value

    num_pennies = int(total_change / penny_value)

    # Calculate the total number of coins
    total_coins = num_quarters + num_dimes + num_nickels + num_pennies
    result = total_coins
    return result

print(solution())