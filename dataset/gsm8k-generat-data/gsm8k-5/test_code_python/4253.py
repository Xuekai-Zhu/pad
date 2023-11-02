def solution():
    cheese_per_ham_sandwich = 2  # Each ham sandwich requires 2 slices of cheese
    cheese_per_grilled_cheese = 3  # Each grilled cheese sandwich requires 3 slices of cheese
    total_cheese = 50  # Joan uses a total of 50 slices of cheese
    ham_sandwiches = 10  # Joan makes 10 ham sandwiches

    # Calculate the remaining cheese after making ham sandwiches
    remaining_cheese = total_cheese - (cheese_per_ham_sandwich * ham_sandwiches)

    # Calculate the number of grilled cheese sandwiches that can be made with the remaining cheese
    grilled_cheese_sandwiches = remaining_cheese / cheese_per_grilled_cheese
    result = grilled_cheese_sandwiches
    return result

print(solution())