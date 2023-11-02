def solution():
    # Calculate the total number of slices needed
    slices_needed = 2 * 3 + 6 * 1

    # Calculate the number of pizzas needed to have at least the number of slices needed
    pizzas_needed = (slices_needed + 3) // 4

    result = pizzas_needed
    return result

print(solution())