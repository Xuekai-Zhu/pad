def solution():
    """David found $12 on the street. He then gave it to his friend Evan who has $1 and needed to buy a watch worth $20. How much does Evan still need?"""
    # Define the initial amount of money Evan has and the cost of the watch
    initial_money = 1
    cost_of_watch = 20

    # Add the money David found to Evan's initial amount
    total_money = initial_money + 12

    # Calculate how much Evan still needs to buy the watch
    remaining_money = cost_of_watch - total_money

    # Display how much Evan still needs
    result = remaining_money
    return result

print(solution())