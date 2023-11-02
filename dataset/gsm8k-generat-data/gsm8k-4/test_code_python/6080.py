def solution():
    """Bob, Tom, Sally, and Jerry had dinner at their favorite pizzeria. They decide to share 2 pizzas. Bob ate half of a pizza on his own. Tom ate one-third of a pizza. Sally wasn't very hungry and only ate one-sixth of a pizza, and Jerry ate a quarter of a pizza. If each pizza is cut into 12 slices, how many slices were left over?"""
    # Define the number of slices per pizza
    slices_per_pizza = 12

    # Calculate the total number of slices eaten
    total_slices_eaten = (1/2 + 1/3 + 1/6 + 1/4) * slices_per_pizza

    # Calculate the total number of slices left over
    slices_leftover = 2 * slices_per_pizza - round(total_slices_eaten)

    # return the result
    result = slices_leftover
    return result

print(solution())