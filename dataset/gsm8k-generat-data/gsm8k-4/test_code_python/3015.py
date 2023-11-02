def solution():
    """Sam has 19 dimes and 6 quarters. She buys 4 candy bars for 3 dimes each and 1 lollipop for 1 quarter. How much money, in cents, does she have left?"""
    # Define the value of a dime and a quarter in cents
    DIME_VALUE = 10
    QUARTER_VALUE = 25

    # Calculate the total value of Sam's dimes and quarters
    total_value = (19 * DIME_VALUE) + (6 * QUARTER_VALUE)

    # Calculate the cost of the candy bars and the lollipop
    candy_bar_cost = 4 * (3 * DIME_VALUE)
    lollipop_cost = 1 * QUARTER_VALUE

    # Calculate the remaining value of Sam's money
    remaining_value = total_value - candy_bar_cost - lollipop_cost

    # return the result
    result = remaining_value
    return result

print(solution())