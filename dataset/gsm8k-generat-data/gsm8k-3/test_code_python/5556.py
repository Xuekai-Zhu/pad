def solution():
    """Delores has some money. She buys a computer for $400 and a printer for $40. If she has $10 left, how much money, in dollars, did Delores have at first?"""
    # Define the cost of the computer and printer
    COMPUTER_COST = 400
    PRINTER_COST = 40

    # Define the amount of money Delores has left
    LEFTOVER = 10

    # Calculate the initial amount of money Delores had
    initial_money = COMPUTER_COST + PRINTER_COST + LEFTOVER

    # Display the initial amount of money
    result = initial_money
    return result

print(solution())