def solution():
    """Todd has $20. He buys 4 candy bars that cost $2 each. How much money in dollars does Todd have left?"""
    # Define the cost of each candy bar
    CANDY_BAR_PRICE = 2

    # Define Todd's initial amount of money
    INITIAL_MONEY = 20

    # Calculate the cost of the 4 candy bars
    candy_bar_cost = CANDY_BAR_PRICE * 4

    # Calculate Todd's remaining amount of money
    remaining_money = INITIAL_MONEY - candy_bar_cost

    # Display Todd's remaining amount of money
    result = remaining_money
    return result

print(solution())