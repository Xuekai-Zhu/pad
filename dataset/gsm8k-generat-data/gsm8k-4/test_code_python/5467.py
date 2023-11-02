def solution():
    """There is a group of 18 people who are ordering pizza. If each person gets 3 slices and each pizza has 9 slices, how many pizzas should they order?"""
    # Define the number of slices per person and per pizza
    slices_per_person = 3
    slices_per_pizza = 9

    # Calculate the total number of slices needed
    total_slices = slices_per_person * 18

    # Calculate the number of pizzas needed
    pizzas_needed = total_slices // slices_per_pizza

    # If there are any leftover slices, add an additional pizza
    if total_slices % slices_per_pizza > 0:
        pizzas_needed += 1

    # return the result
    result = pizzas_needed
    return result

print(solution())