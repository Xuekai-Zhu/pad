def solution():
    # Define the amount John spent and the amount he received in change
    amount_spent = 20 - 8
    change_received = 8

    # Calculate the number of Slurpees John bought
    slurpee_cost = 2
    num_slurpees = amount_spent // slurpee_cost

    result = num_slurpees
    return result

print(solution())