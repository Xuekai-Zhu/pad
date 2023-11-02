def solution():
    """Darwin has 600$. He spent 1/3 of it on gas for his car, and 1/4 of what was left on food. How much money did he have left?"""
    # Define Darwin's initial amount of money
    initial_money = 600

    # Calculate the amount of money spent on gas
    gas_spending = initial_money / 3

    # Calculate the amount of money left after gas spending
    money_left = initial_money - gas_spending

    # Calculate the amount of money spent on food
    food_spending = money_left / 4

    # Calculate the amount of money left after food spending
    money_left_final = money_left - food_spending

    result = money_left_final
    return result

print(solution())