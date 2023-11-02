def solution():
    # Calculate the cost of the ingredients
    flour_cost = 4 * 2
    sugar_cost = 2 * 2
    butter_cost = 2.5
    egg_cost = 0.5 * 2
    total_cost = flour_cost + sugar_cost + butter_cost + egg_cost

    # Calculate the cost per slice
    cost_per_slice = total_cost / 6

    # Calculate the cost of the slices her mother enjoyed
    mother_slices_cost = cost_per_slice * 2

    # Calculate the cost of the cake that Kevin ate
    kevin_slices_cost = cost_per_slice * 4

    # Calculate the amount the dog ate cost
    dog_eaten_cost = kevin_slices_cost - mother_slices_cost
    result = dog_eaten_cost
    return result

print(solution())