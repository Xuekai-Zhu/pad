def solution():
    """Darwin has 600$. He spent 1/3 of it on gas for his car, and 1/4 of what was left on food. How much money did he have left?"""
    # Define the initial amount of money Darwin has
    initial_money = 600

    # Calculate how much Darwin spent on gas for his car
    gas_spending = initial_money / 3

    # Calculate how much money Darwin has left after spending on gas
    money_left = initial_money - gas_spending

    # Calculate how much Darwin spent on food
    food_spending = money_left / 4

    # Calculate how much money Darwin has left after spending on food
    money_left -= food_spending

    # Display how much money Darwin has left
    result = money_left
    return result

print(solution())