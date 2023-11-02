def solution():
    people = 18
    slices_per_person = 3
    slices_per_pizza = 9
    pizzas_needed = people * slices_per_person / slices_per_pizza
    result = pizzas_needed
    return result

print(solution())