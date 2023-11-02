def solution():
    """
    At a pool party, there are 4 pizzas cut into 12 slices each. If the guests eat 39 slices, how many slices are left?
    """
    # Define the number of pizzas and slices per pizza
    pizzas = 4
    slices_per_pizza = 12

    # Calculate the total number of slices
    total_slices = pizzas * slices_per_pizza

    # Calculate the number of slices remaining after the guests eat 39 slices
    slices_remaining = total_slices - 39

    # Display the number of slices remaining
    result = slices_remaining
    return result

print(solution())