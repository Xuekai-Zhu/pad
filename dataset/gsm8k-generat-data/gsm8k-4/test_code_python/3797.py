def solution():
    """Ivan had $10 and spent 1/5 of it on cupcakes. He then spent some money on a milkshake and had only $3 left. How much is the milkshake?"""
    # Define the initial amount of money Ivan had
    initial_money = 10

    # Calculate the amount of money Ivan spent on cupcakes
    cupcakes_cost = initial_money / 5

    # Calculate the amount of money Ivan had left
    remaining_money = initial_money - cupcakes_cost - 3

    # Calculate the cost of the milkshake
    milkshake_cost = remaining_money

    # Return the result
    result = milkshake_cost
    return result

print(solution())