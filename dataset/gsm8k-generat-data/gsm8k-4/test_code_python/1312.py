def solution():
    """A merchant bought 15 keyboards and 25 printers for a total of $2050. If a keyboard costs $20, how much does a printer cost?"""
    # Define the number of keyboards and printers, and the total cost
    num_keyboards = 15
    num_printers = 25
    total_cost = 2050

    # Calculate the total cost of the keyboards
    keyboard_cost = num_keyboards * 20

    # Calculate the total cost of the printers
    printer_cost = total_cost - keyboard_cost

    # Calculate the cost per printer
    cost_per_printer = printer_cost / num_printers

    # Return the result
    result = cost_per_printer
    return result

print(solution())