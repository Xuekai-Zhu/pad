def solution():
    """Todd has $20. He buys 4 candy bars that cost $2 each. How much money in dollars does Todd have left?"""
    # Define the initial amount of money Todd has
    initial_money = 20

    # Calculate the cost of the candy bars
    candy_bars_cost = 4 * 2

    # Calculate the remaining amount of money Todd has after buying the candy bars
    remaining_money = initial_money - candy_bars_cost

    # return the result
    result = remaining_money
    return result

print(solution())