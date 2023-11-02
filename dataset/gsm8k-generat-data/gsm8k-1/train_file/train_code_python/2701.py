def solution():
    """Stephen ordered 2 large pizzas, both cut into 12 slices. He ate 25% of the pizza. His friend Pete ate 50% of the remaining pizza. How many slices are left over?"""
    pizzas_ordered = 2
    slices_per_pizza = 12
    total_slices = pizzas_ordered * slices_per_pizza
    stephen_slices = total_slices * 0.25
    remaining_slices = total_slices - stephen_slices
    pete_slices = remaining_slices * 0.5
    slices_left = remaining_slices - pete_slices
    result = slices_left
    return result

print(solution())