def solution():
    # Calculate the total number of slices needed
    slices_needed = 18 * 3  # each person gets 3 slices
    pizzas_needed = slices_needed / 9  # each pizza has 9 slices
    result = pizzas_needed
    return result

print(solution())