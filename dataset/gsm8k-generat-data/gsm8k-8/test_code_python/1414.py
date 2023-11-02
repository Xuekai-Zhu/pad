def solution():
    # Define the initial cost
    initial_cost = 150

    # Calculate the cashback amount
    cashback = 0.1 * initial_cost

    # Calculate the final cost after cashback and mail-in rebate
    final_cost = initial_cost - cashback - 25

    result = final_cost
    return result

print(solution())