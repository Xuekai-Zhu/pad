def solution():
    
    cappuccinos_cost = 2
    iced_teas_cost = 3
    cafe_lattes_cost = 1.5
    espressos_cost = 1
    num_cappuccinos = 3
    num_iced_teas = 2
    num_cafe_lattes = 2
    num_espressos = 2
    total_cost = cappuccinos_cost*num_cappuccinos + iced_teas_cost*num_iced_teas + cafe_lattes_cost*num_cafe_lattes + espressos_cost*num_espressos
    change = 20 - total_cost
    result = change
    return result

print(solution())