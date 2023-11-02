def solution():
    people = 8
    pizza_slices = 4
    slices_per_person = 3
    needed_pizzas = people * slices_per_person / pizza_slices
    result = needed_pizzas
    return result

print(solution())