def solution():
    # Calculate the cost of 1 dozen of doughnuts
    cost_per_dozen = 8/1

    # Calculate the cost of 2 dozens of doughnuts
    cost_per_two_dozen = 14/2

    # Calculate the savings per set when buying 2 dozens instead of 1 dozen
    saving_per_set = cost_per_dozen * 2 - cost_per_two_dozen

    # Calculate the total savings when buying 3 sets of 2 dozens instead of 6 sets of 1 dozen
    total_savings = saving_per_set * 3

    result = total_savings
    return result

print(solution())