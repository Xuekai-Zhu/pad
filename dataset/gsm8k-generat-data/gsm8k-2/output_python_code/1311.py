def solution():
    """A merchant bought 15 keyboards and 25 printers for a total of $2050. If a keyboard costs $20, how much does a printer cost?"""
    keyboard_price = 20
    total_price = 2050
    total_quantity = 15 + 25
    keyboard_quantity = 15
    keyboard_total_price = keyboard_quantity * keyboard_price
    printer_total_price = total_price - keyboard_total_price
    printer_quantity = total_quantity - keyboard_quantity
    printer_price = printer_total_price / printer_quantity
    result = printer_price
    return result

print(solution())