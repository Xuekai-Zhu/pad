def solution():
    """Randy has some money. He spent $10 buying his lunch. He spent a quarter of the money he had left on an ice cream cone. If the ice cream cone cost $5, what is the amount of money, in dollars, Randy had at first?"""
    # Define the cost of the lunch and the ice cream cone
    LUNCH_COST = 10
    ICE_CREAM_COST = 5

    # Define the fraction of money spent on the ice cream cone
    ICE_CREAM_FRACTION = 1/4

    # Calculate the amount of money Randy had left after buying his lunch
    money_left = amount_spent - LUNCH_COST

    # Calculate the amount Randy spent on the ice cream cone
    ice_cream_spent = money_left * ICE_CREAM_FRACTION

    # Calculate the amount of money Randy had at first
    amount_at_first = (ice_cream_spent + ICE_CREAM_COST) / (1 - ICE_CREAM_FRACTION)

    # Display the amount of money Randy had at first
    result = amount_at_first
    return result

print(solution())