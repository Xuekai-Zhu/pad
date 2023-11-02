def solution():
    lemon_juice_per_lemon = 4  # Each lemon provides 4 tablespoons of lemon juice
    tablespoons_per_dozen = 12  # Jose needs 12 tablespoons of lemon juice to make a dozen cupcakes
    dozens_of_cupcakes = 3  # Jose wants to make 3 dozen cupcakes

    # Calculate the total tablespoons of lemon juice needed
    total_lemon_juice = tablespoons_per_dozen * dozens_of_cupcakes

    # Calculate the number of lemons needed
    lemons_needed = total_lemon_juice / lemon_juice_per_lemon
    result = lemons_needed
    return result

print(solution())