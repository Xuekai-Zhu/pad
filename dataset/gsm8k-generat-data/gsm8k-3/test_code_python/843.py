def solution():
    """Randy has $30. He spent $10 buying his lunch. He spent a quarter of the money he had left on an ice cream cone. What is the amount of money, in dollars, Randy has left?"""
    # Define Randy's starting money and lunch cost
    starting_money = 30
    lunch_cost = 10

    # Calculate Randy's remaining money after buying lunch
    remaining_money = starting_money - lunch_cost

    # Calculate the cost of the ice cream cone and subtract from remaining money
    ice_cream_cost = remaining_money / 4
    remaining_money -= ice_cream_cost

    # Display the amount of money Randy has left
    result = remaining_money
    return result

print(solution())