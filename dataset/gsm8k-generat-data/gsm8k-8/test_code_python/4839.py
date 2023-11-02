def solution():
    # Define the number of cupcakes and the cost per cupcake
    num_cupcakes = 12
    cost_per_cupcake = 1.5

    # Calculate the total cost of the cupcakes
    total_cost = num_cupcakes * cost_per_cupcake

    # Calculate the cost per person
    cost_per_person = total_cost / 2

    result = cost_per_person
    return result

print(solution())