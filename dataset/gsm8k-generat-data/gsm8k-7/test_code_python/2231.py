def solution():
    num_couple_slices = 3  # per person
    num_children_slices = 1  # per child
    num_adults = 2
    num_children = 6
    total_slices = (num_couple_slices * num_adults) + (num_children_slices * num_children)
    num_pizzas = (total_slices + 3) // 4 # Round up to nearest whole pizza
    result = num_pizzas
    return result

print(solution())