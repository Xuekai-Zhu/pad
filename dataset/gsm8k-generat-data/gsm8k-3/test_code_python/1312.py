def solution():
    """A merchant bought 15 keyboards and 25 printers for a total of $2050. If a keyboard costs $20, how much does a printer cost?"""
    # Define the cost of a keyboard
    KEYBOARD_PRICE = 20

    # Define the number of keyboards and printers purchased
    keyboard_quantity = 15
    printer_quantity = 25

    # Calculate the total cost of the keyboards
    keyboard_cost = keyboard_quantity * KEYBOARD_PRICE

    # Calculate the total cost of the printers
    total_cost = 2050
    printer_cost = (total_cost - keyboard_cost) / printer_quantity

    # Display the cost of a printer
    result = printer_cost
    return result

print(solution())