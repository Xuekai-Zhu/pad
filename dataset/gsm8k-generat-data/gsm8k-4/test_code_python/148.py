def solution():
    """Winwin won $50 in a lottery. She paid 20% for the tax and she paid $5 for the processing fee. How much was she able to take home?"""
    # Define the initial winnings
    winnings = 50

    # Calculate the amount of tax
    tax = winnings * 0.2

    # Calculate the total deductions
    deductions = tax + 5

    # Calculate the amount of money Winwin takes home
    take_home = winnings - deductions

    result = take_home
    return result

print(solution())