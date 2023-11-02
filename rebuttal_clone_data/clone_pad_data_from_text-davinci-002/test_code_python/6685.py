def solution():
    pizzas_Craig_first_day = 40
    pizzas_Craig_second_day = pizzas_Craig_first_day + 60
    pizzas_Heather_first_day = 4 * pizzas_Craig_first_day
    pizzas_Heather_second_day = pizzas_Heather_first_day - 20
    total_pizzas = pizzas_Craig_second_day + pizzas_Heather_second_day
    result = total_pizzas
    return result

print(solution())