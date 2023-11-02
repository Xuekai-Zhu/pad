def solution():
    """Twelve coworkers go out for lunch together and order three pizzas. Each pizza is cut into eight slices. If each person gets the same number of slices, how many slices will each person get?"""
    # Define the number of coworkers and pizzas
    num_coworkers = 12
    num_pizzas = 3

    # Calculate the total number of slices
    total_slices = num_pizzas * 8

    # Calculate the number of slices per coworker
    slices_per_coworker = total_slices / num_coworkers

    # return the result
    result = slices_per_coworker
    return result

print(solution())