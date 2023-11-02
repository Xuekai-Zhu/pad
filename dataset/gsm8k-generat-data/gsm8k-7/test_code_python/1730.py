def solution():
    cost_of_1_dozen = 8
    cost_of_2_dozen = 14
    num_sets_of_1_dozen = 6
    num_sets_of_2_dozen = 3

    # Calculate the cost of buying 6 sets of 1 dozen
    cost_of_6_sets_of_1_dozen = num_sets_of_1_dozen * cost_of_1_dozen

    # Calculate the cost of buying 3 sets of 2 dozens
    cost_of_3_sets_of_2_dozen = num_sets_of_2_dozen * cost_of_2_dozen

    # Calculate the amount saved by buying 3 sets of 2 dozens instead of 6 sets of 1 dozen
    amount_saved = cost_of_6_sets_of_1_dozen - cost_of_3_sets_of_2_dozen
    result = amount_saved
    return result

print(solution())