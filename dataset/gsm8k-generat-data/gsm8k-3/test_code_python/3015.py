def solution():
    """Sam has 19 dimes and 6 quarters. She buys 4 candy bars for 3 dimes each and 1 lollipop for 1 quarter. How much money, in cents, does she have left?"""
    # Define the value of each coin
    DIME_VALUE = 10
    QUARTER_VALUE = 25

    # Define the number of each coin Sam has
    num_dimes = 19
    num_quarters = 6

    # Calculate the total value of Sam's coins
    total_value = num_dimes * DIME_VALUE + num_quarters * QUARTER_VALUE

    # Calculate the cost of the candy bars and lollipop
    candy_bar_cost = 3 * 4 # 4 candy bars at 3 dimes each
    lollipop_cost = 1 * QUARTER_VALUE

    # Calculate the total cost of the purchases
    total_cost = candy_bar_cost + lollipop_cost

    # Calculate the remaining amount of money Sam has
    remaining_money = total_value - total_cost

    # Display the remaining amount of money in cents
    result = remaining_money
    return result

print(solution())