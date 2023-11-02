def solution():
    """Jeremy's uncle gave him $50 to spend on basketball equipment. He bought 5 jerseys that cost $2 each, a basketball that cost $18, and a pair of shorts that cost $8. How much money does Jeremy have left?"""
    # Define the initial amount of money Jeremy has
    initial_money = 50

    # Calculate the cost of 5 jerseys
    jerseys_cost = 5 * 2

    # Calculate the total cost of all the items purchased
    total_cost = jerseys_cost + 18 + 8

    # Calculate the money Jeremy has left
    left_over = initial_money - total_cost

    # Return the result
    result = left_over
    return result

print(solution())