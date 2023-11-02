def solution():
    # Calculate the total number of slices needed
    slices_needed = 10 * 2

    # Calculate the number of pizzas needed (round up to the nearest whole number)
    pizzas_needed = math.ceil(slices_needed / 4)

    result = pizzas_needed
    return result

print(solution())