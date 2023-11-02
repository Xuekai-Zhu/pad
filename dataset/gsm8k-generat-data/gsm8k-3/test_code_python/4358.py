def solution():
    """A mother is serving pizza at her son's birthday party.  After buying 5 pizzas, she must decide how many slices to divide each pizza into so that everyone at the party ends up with an equal number of slices.  There are a total of 20 children at the party, and she can choose to divide each pizza into either 6, 8, or 10 slices.  Assuming she does not want to throw away any pizza, how should many slices should she choose to divide the pizzas into to make sure everyone receives an equal amount?"""
    # Define the number of pizzas and children
    num_pizzas = 5
    num_children = 20

    # Define the slice options and initialize the minimum difference to a large number
    slice_options = [6, 8, 10]
    min_difference = float('inf')

    # Iterate through all possible combinations of slice options and calculate the difference
    for i in range(len(slice_options)):
        for j in range(len(slice_options)):
            for k in range(len(slice_options)):
                slices_1 = slice_options[i]
                slices_2 = slice_options[j]
                slices_3 = slice_options[k]
                total_slices = num_pizzas * (slices_1 + slices_2 + slices_3)
                difference = abs(total_slices - (num_children * slices_1))
                if difference < min_difference:
                    min_difference = difference
                    optimal_slices = slices_1

    # Display the optimal number of slices per pizza
    result = optimal_slices
    return result

print(solution())