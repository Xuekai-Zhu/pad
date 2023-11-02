def solution():
    num_ham_sandwiches = 10
    slices_per_ham_sandwich = 2
    slices_per_grilled_cheese_sandwich = 3
    total_slices = 50

    # Calculate the total number of slices of cheese used for ham sandwiches
    ham_slices = num_ham_sandwiches * slices_per_ham_sandwich

    # Calculate the total number of slices of cheese used for grilled cheese sandwiches
    grilled_cheese_slices = total_slices - ham_slices

    # Calculate the total number of grilled cheese sandwiches made
    num_grilled_cheese_sandwiches = grilled_cheese_slices / slices_per_grilled_cheese_sandwich
    result = num_grilled_cheese_sandwiches
    return result

print(solution())