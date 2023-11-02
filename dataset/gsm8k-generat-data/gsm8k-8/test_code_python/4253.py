def solution():
    # Define the number of slices of cheese needed for a ham sandwich and a grilled cheese sandwich
    ham_sandwich_cheese = 2
    grilled_cheese_cheese = 3

    # Define the number of ham sandwiches
    ham_sandwiches = 10

    # Calculate the total number of slices of cheese used for the ham sandwiches
    total_ham_cheese = ham_sandwiches * ham_sandwich_cheese

    # Calculate the number of slices of cheese remaining for the grilled cheese sandwiches
    remaining_cheese = 50 - total_ham_cheese

    # Calculate the number of grilled cheese sandwiches that can be made with the remaining cheese
    grilled_cheese_sandwiches = remaining_cheese // grilled_cheese_cheese

    result = grilled_cheese_sandwiches
    return result

print(solution())