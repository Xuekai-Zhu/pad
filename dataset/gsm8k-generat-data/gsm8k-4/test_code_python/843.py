def solution():
    """Randy has $30. He spent $10 buying his lunch. He spent a quarter of the money
    he had left on an ice cream cone. What is the amount of money, in dollars, Randy has left?"""
    # Define the initial amount of money and the cost of lunch
    initial_money = 30
    lunch_cost = 10

    # Calculate the remaining amount of money after buying lunch
    remaining_money = initial_money - lunch_cost

    # Calculate the cost of the ice cream cone
    ice_cream_cost = remaining_money / 4

    # Calculate the final amount of money remaining
    final_money = remaining_money - ice_cream_cost

    # Return the result
    result = final_money
    return result

print(solution())