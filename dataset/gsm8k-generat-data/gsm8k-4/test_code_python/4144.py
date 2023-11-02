def solution():
    """You have 32$ to spend on groceries. You buy a loaf of bread for 3$, a candy bar for 2$, and 1/3 of whats left on a Turkey. How much money do you have left?"""
    # Define the initial amount of money and the cost of the bread and candy bar
    money = 32
    bread_cost = 3
    candy_bar_cost = 2

    # Calculate the money left after buying bread and candy bar
    money_left = money - bread_cost - candy_bar_cost

    # Calculate the cost of the turkey
    turkey_cost = money_left / 3

    # Calculate the money left after buying turkey
    money_left = money_left - turkey_cost

    # return the result
    result = money_left
    return result

print(solution())