def solution():
    num_keyboards = 15
    keyboard_price = 20

    total_spent = 2050

    # Calculate the total cost of all keyboards
    total_keyboard_cost = num_keyboards * keyboard_price

    # Calculate the cost of all printers
    cost_of_printers = total_spent - total_keyboard_cost

    # Calculate the cost of one printer
    price_of_printer = cost_of_printers / 25
    result = price_of_printer
    return result

print(solution())