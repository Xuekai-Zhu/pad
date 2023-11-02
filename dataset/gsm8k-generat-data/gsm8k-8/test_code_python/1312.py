def solution():
    # Define the number of keyboards and printers
    num_keyboards = 15
    num_printers = 25

    # Calculate the total cost of the purchases
    total_cost = 2050

    # Calculate the total cost of the keyboards
    keyboard_cost = num_keyboards * 20

    # Calculate the cost of the printers
    printer_cost = (total_cost - keyboard_cost) / num_printers
    result = printer_cost
    return result

print(solution())