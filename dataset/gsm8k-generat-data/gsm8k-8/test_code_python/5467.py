def solution():
    # Calculate the total number of slices needed
    total_slices = 18 * 3

    # Calculate the number of pizzas needed, rounding up to the nearest integer
    pizzas_needed = math.ceil(total_slices / 9)

    result = pizzas_needed
    return result

print(solution())