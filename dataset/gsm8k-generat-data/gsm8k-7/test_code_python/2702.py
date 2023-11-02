def solution():
    num_pizzas = 2
    slices_per_pizza = 12
    total_slices = num_pizzas * slices_per_pizza
    stephen_percent = 0.25
    pete_percent = 0.5
    stephen_slices = total_slices * stephen_percent
    remaining_slices = total_slices - stephen_slices
    pete_slices = remaining_slices * pete_percent
    slices_left = remaining_slices - pete_slices
    result = slices_left
    return result

print(solution())