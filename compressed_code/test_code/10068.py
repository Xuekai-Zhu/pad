def solution():
    
    people = 18
    slices_per_person = 3
    slices_per_pizza = 9
    total_slices = people * slices_per_person
    pizzas_needed = total_slices // slices_per_pizza + (1 if total_slices % slices_per_pizza != 0 else 0)
    result = pizzas_needed
    return result

print(solution())