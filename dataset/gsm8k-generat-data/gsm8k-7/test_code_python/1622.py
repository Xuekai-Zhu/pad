def solution():
    tablespoons_per_lemon = 4
    tablespoons_per_dozen = 12
    cupcakes_per_dozen = 12
    num_dozen_cupcakes = 3

    # Calculate the total number of tablespoons of lemon juice needed
    total_tablespoons = tablespoons_per_dozen * cupcakes_per_dozen * num_dozen_cupcakes

    # Calculate the total number of lemons needed
    num_lemons = total_tablespoons / tablespoons_per_lemon
    result = num_lemons
    return result

print(solution())