def solution():
    
    initial_budget = 1500
    machine_cost = 1090
    screen_keyboard_mouse = 1090
    scanner_cost =157
    cd_burner_cost = 74
    printer_cost = 102
    total_money = initial_budget - machine_cost - screen_keyboard_mouse + scanner_cost + cd_burner_cost + printer_cost
    result = total_money
    return result

print(solution())