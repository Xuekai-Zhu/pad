def solution():
    # Define the amount John paid and the amount of change
    paid = 20
    change = 14

    # Calculate the total cost of the sodas
    total_cost = paid - change

    # Calculate the cost of each soda
    cost_per_soda = total_cost / 3
    result = cost_per_soda
    return result

print(solution())