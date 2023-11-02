def solution():
    
    couple_slices = 3
    children_slices = 1
    total_slices = couple_slices * 2 + children_slices * 6
    slices_per_pizza = 4
    pizzas_needed = (total_slices + slices_per_pizza - 1) // slices_per_pizza
    result = pizzas_needed
    return result

print(solution())