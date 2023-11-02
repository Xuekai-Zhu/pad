def solution():
    num_cakes = 2
    num_flour_per_cake = 2
    cost_per_package = 3

    # Calculate the total number of flour packages needed
    total_flour = num_cakes * num_flour_per_cake

    # Calculate the total cost of all the flour packages
    total_cost = total_flour * cost_per_package
    result = total_cost
    return result

print(solution())