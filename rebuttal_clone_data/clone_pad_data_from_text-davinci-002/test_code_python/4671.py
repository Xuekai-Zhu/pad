def solution():
    sandwich_pizzas = 2
    regular_pizzas = 12 - sandwich_pizzas
    total_pizzas = regular_pizzas + sandwich_pizzas
    minutes_to_deliver = 40
    minutes_per_stop = minutes_to_deliver / total_pizzas
    result = minutes_per_stop
    return result

print(solution())