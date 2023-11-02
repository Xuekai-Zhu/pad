def solution():
    keyboard_price = 20  # cost of one keyboard
    total_items = 15 + 25  # total number of items (keyboards + printers)
    total_cost = 2050  # total cost of all items

    # Calculate the cost of all the keyboards
    keyboard_cost = 15 * keyboard_price

    # Calculate the cost of all the printers
    printer_cost = total_cost - keyboard_cost

    # Calculate the cost of one printer
    printer_price = printer_cost / 25
    result = printer_price
    return result

print(solution())