def solution():
    money = 100  # Tyler has $100
    cost_of_scissors = 8 * 5  # Tyler buys 8 scissors for $5 each
    cost_of_erasers = 10 * 4  # Tyler buys 10 erasers for $4 each

    # Calculate the total cost of the items Tyler bought
    total_cost = cost_of_scissors + cost_of_erasers

    # Calculate how much money remains after Tyler buys the items
    remaining_money = money - total_cost
    result = remaining_money
    return result

print(solution())