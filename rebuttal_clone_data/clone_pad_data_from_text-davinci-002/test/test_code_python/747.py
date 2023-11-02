def solution():
    keyboards = 15
    printers = 25
    total_cost = 2050
    cost_of_keyboards = 15 * 20
    cost_of_printers = total_cost - cost_of_keyboards
    printer_cost = cost_of_printers / printers
    result = printer_cost
    return result

print(solution())