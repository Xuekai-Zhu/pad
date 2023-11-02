def solution():
    """Tyler has $100. If he buys 8 scissors for $5 each and 10 erasers for $4 each, how much of his money remains?"""
    # Define the starting amount of money and the cost of scissors and erasers
    starting_money = 100
    scissors_cost = 5
    erasers_cost = 4

    # Calculate the total cost of the scissors and erasers
    total_cost = (8 * scissors_cost) + (10 * erasers_cost)

    # Calculate how much money is left after the purchase
    money_left = starting_money - total_cost

    result = money_left
    return result

print(solution())