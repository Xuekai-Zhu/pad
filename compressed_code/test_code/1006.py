def solution():
    
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