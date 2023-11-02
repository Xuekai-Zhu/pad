def solution():
    # Calculate the cost of 1 dozen doughnuts
    cost_per_dozen = 8

    # Calculate the cost of 2 dozens doughnuts
    cost_per_two_dozen = 14
    cost_per_dozen_two = cost_per_two_dozen / 2  # Divide the cost by 2 to get the cost of 1 dozen

    # Calculate the total cost of buying 3 sets of 2 dozens
    cost_3_sets = 3 * cost_per_two_dozen

    # Calculate the total cost of buying 6 sets of 1 dozen
    cost_6_sets = 6 * cost_per_dozen

    # Calculate the amount saved by buying 3 sets of 2 dozens instead of 6 sets of 1 dozen
    amount_saved = cost_6_sets - cost_3_sets
    result = amount_saved
    return result

print(solution())