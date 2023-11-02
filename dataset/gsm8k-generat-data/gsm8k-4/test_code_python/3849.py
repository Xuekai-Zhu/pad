def solution():
    """Randy has some money. He spent $10 buying his lunch. He spent a quarter of the money he had left on an ice cream cone. If the ice cream cone cost $5, what is the amount of money, in dollars, Randy had at first?"""
    # Define the initial amount of money
    initial_money = None

    # Randy spent $10 on lunch
    initial_money = 10

    # Calculate the amount of money he had left
    money_left = initial_money - 10

    # Randy spent a quarter of the money he had left on an ice cream cone
    ice_cream_cost = 5
    money_spent_on_ice_cream = money_left / 4

    # Calculate the amount of money Randy had at first
    initial_money = money_left + money_spent_on_ice_cream + ice_cream_cost

    result = initial_money
    return result

print(solution())