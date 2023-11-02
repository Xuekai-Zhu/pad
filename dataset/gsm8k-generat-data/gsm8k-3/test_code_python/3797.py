def solution():
    """Ivan had $10 and spent 1/5 of it on cupcakes. He then spent some money on a milkshake and had only $3 left. How much is the milkshake?"""
    # Define the initial amount of money Ivan had
    initial_amount = 10

    # Calculate the amount of money Ivan spent on cupcakes
    cupcakes_spent = initial_amount * (1/5)

    # Calculate the amount of money Ivan had left after buying cupcakes
    amount_left = initial_amount - cupcakes_spent

    # Calculate the cost of the milkshake
    milkshake_cost = amount_left - 3

    # Display the cost of the milkshake
    result = milkshake_cost
    return result

print(solution())