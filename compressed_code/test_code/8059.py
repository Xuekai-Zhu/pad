def solution():
    
    curtain_price = 30
    print_price = 15
    number_of_curtains = 2
    number_of_prints = 9
    installation_service_cost = 50
    total_cost = (curtain_price * number_of_curtains) + (print_price * number_of_prints) + installation_service_cost
    result = total_cost
    return result

print(solution())