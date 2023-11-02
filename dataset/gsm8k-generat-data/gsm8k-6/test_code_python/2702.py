def solution():
    # Calculate the total number of slices
    total_slices = 2 * 12  # 2 large pizzas, each cut into 12 slices
    # Calculate the number of slices Stephen ate
    stephen_slices = 0.25 * total_slices  # Stephen ate 25% of the pizza
    # Calculate the number of slices remaining after Stephen ate
    remaining_slices = total_slices - stephen_slices
    # Calculate the number of slices Pete ate
    pete_slices = 0.5 * remaining_slices  # Pete ate 50% of the remaining pizza
    # Calculate the number of slices remaining
    slices_left = remaining_slices - pete_slices
    result = slices_left
    return result

print(solution())