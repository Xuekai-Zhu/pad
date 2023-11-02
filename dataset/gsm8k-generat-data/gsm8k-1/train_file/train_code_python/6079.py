def solution():
    """Bob, Tom, Sally, and Jerry had dinner at their favorite pizzeria. They decide to share 2 pizzas. Bob ate half of a pizza on his own. Tom ate one-third of a pizza. Sally wasn't very hungry and only ate one-sixth of a pizza, and Jerry ate a quarter of a pizza. If each pizza is cut into 12 slices, how many slices were left over?"""
    num_pizzas = 2
    slices_per_pizza = 12
    total_slices = num_pizzas * slices_per_pizza
    slices_eaten = (1/2 + 1/3 + 1/6 + 1/4) * slices_per_pizza
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())