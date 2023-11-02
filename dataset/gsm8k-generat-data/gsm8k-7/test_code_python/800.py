def solution():
    cappuccino_cost = 2
    iced_tea_cost = 3
    cafe_latte_cost = 1.5
    espresso_cost = 1

    num_cappuccinos = 3
    num_iced_teas = 2
    num_cafe_lattes = 2
    num_espressos = 2

    total_cost = (cappuccino_cost*num_cappuccinos) + (iced_tea_cost*num_iced_teas) + (cafe_latte_cost*num_cafe_lattes) + (espresso_cost*num_espressos)

    change = 20 - total_cost
    result = change
    return result

print(solution())