def solution():
    # Calculate the total number of slices needed
    total_slices = 2 * 3 + 6 * 1  # the couple wants 3 slices each and the children want 1 slice each
    # Calculate the number of pizzas needed
    pizzas_needed = (total_slices + 3) // 4  # round up to the nearest whole pizza
    result = pizzas_needed
    return result

print(solution())