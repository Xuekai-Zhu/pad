def solution():
    """Josh has some money. He spent $1.75 on a drink, and then spent another $1.25. If he had $6 left, how much money, in dollars, did Josh have at first?"""
    # Define the price of the drink and the second expense
    drink_price = 1.75
    second_expense = 1.25

    # Calculate the total amount spent
    total_spent = drink_price + second_expense

    # Calculate the initial amount of money Josh had
    initial_amount = total_spent + 6

    # return the result
    result = initial_amount
    return result

print(solution())