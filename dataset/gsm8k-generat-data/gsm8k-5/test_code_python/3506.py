def solution():
    cost_of_candy = 0.44  # The candy costs $0.44
    paid_with = 1.00  # Rosie pays with a $1 bill

    # Calculate the change that Rosie will receive
    change = paid_with - cost_of_candy

    # Calculate the number of coins needed for the change, starting with the largest coin denomination
    num_quarters = int(change / 0.25)
    change -= num_quarters * 0.25

    num_dimes = int(change / 0.10)
    change -= num_dimes * 0.10

    num_nickels = int(change / 0.05)
    change -= num_nickels * 0.05

    num_pennies = int(change / 0.01)

    # Calculate the total number of coins Rosie will receive
    total_num_coins = num_quarters + num_dimes + num_nickels + num_pennies
    result = total_num_coins
    return result

print(solution())