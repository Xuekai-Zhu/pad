def solution():
    """Bob, Tom, Sally, and Jerry had dinner at their favorite pizzeria. They decide to share 2 pizzas. Bob ate half of a pizza on his own. Tom ate one-third of a pizza. Sally wasn't very hungry and only ate one-sixth of a pizza, and Jerry ate a quarter of a pizza. If each pizza is cut into 12 slices, how many slices were left over?"""
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 12

    # Calculate the total number of slices eaten
    slices_eaten = (0.5 + (1/3) + (1/6) + 0.25) * SLICES_PER_PIZZA

    # Calculate the number of slices left over
    slices_left = (2 * SLICES_PER_PIZZA) - slices_eaten

    # Display the number of slices left over
    result = slices_left
    return result

print(solution())