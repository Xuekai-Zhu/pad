def solution():
    total_money_given = 20
    cost_per_slurpee = 2
    change_received = 8

    # Calculate the total cost of all the Slurpees John bought
    total_slurpees_cost = total_money_given - change_received

    # Calculate the number of Slurpees John bought
    num_slurpees = total_slurpees_cost / cost_per_slurpee
    result = num_slurpees
    return result

print(solution())