def solution():
    
    keyboard_cost = 20
    total_cost = 2050
    num_keyboards = 15
    num_printers = 25
    total_keyboards_cost = num_keyboards * keyboard_cost
    printer_cost = (total_cost - total_keyboards_cost) / num_printers
    result = printer_cost
    return result

print(solution())