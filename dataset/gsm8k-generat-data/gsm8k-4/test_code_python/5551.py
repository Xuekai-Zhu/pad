def solution():
    """Delores has $450. She buys a computer for $400 and a printer for $40. How much money, in dollars, does Delores have left?"""
    # Define the initial amount of money Delores has
    initial_money = 450

    # Define the cost of the computer and printer
    computer_cost = 400
    printer_cost = 40

    # Calculate the amount of money Delores has left after buying the computer and printer
    remaining_money = initial_money - computer_cost - printer_cost

    # Return the result
    result = remaining_money
    return result

print(solution())