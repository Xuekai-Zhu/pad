def solution():
    num_pizzas = 5
    num_children = 20

    # Set the possible number of slices per pizza
    possible_slices = [6, 8, 10]

    # Try each possible number of slices
    for num_slices in possible_slices:
        # Calculate the total number of slices for all pizzas
        total_slices = num_pizzas * num_slices

        # Check if the total number of slices can be evenly divided among the children
        if total_slices % num_children == 0:
            result = num_slices
            return result

    # If no possible number of slices works, return an error message
    result = "No solution found"
    return result

print(solution())