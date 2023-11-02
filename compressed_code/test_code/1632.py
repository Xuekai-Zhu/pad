def solution():
    
    num_people = 10
    slices_per_person = 2
    slices_per_pizza = 4
    total_slices_needed = num_people * slices_per_person
    pizzas_needed = total_slices_needed / slices_per_pizza
    result = pizzas_needed
    return result

print(solution())