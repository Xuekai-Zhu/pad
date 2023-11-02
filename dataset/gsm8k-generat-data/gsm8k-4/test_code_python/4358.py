def solution():
    """A mother is serving pizza at her son's birthday party. After buying 5 pizzas, she must decide how many slices to divide each pizza into so that everyone at the party ends up with an equal number of slices. There are a total of 20 children at the party, and she can choose to divide each pizza into either 6, 8, or 10 slices. Assuming she does not want to throw away any pizza, how should many slices should she choose to divide the pizzas into to make sure everyone receives an equal amount?"""
    # Define the number of pizzas and children
    num_pizzas = 5
    num_children = 20

    # Define the possible number of slices per pizza
    slices_per_pizza = [6, 8, 10]

    # Calculate the total number of slices that will be needed
    total_slices_needed = num_children * slices_per_pizza[0] * num_pizzas

    # Try each possible number of slices per pizza and find the one that results in an equal number of slices per child
    for num_slices in slices_per_pizza:
        if total_slices_needed % (num_slices * num_pizzas) == 0:
            slices_per_child = total_slices_needed / (num_children * num_pizzas)
            result = num_slices
            break

    return result

print(solution())