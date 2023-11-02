def solution():
    """Bob, Tom, Sally, and Jerry had dinner at their favorite pizzeria. They decide to share 2 pizzas. Bob ate half of a pizza on his own. Tom ate one-third of a pizza. Sally wasn't very hungry and only ate one-sixth of a pizza, and Jerry ate a quarter of a pizza. If each pizza is cut into 12 slices, how many slices were left over?"""
    total_slices = 2 * 12
    slices_consumed = 6 + 4 + 2 + 3
    slices_left = total_slices - slices_consumed
    result = slices_left
    return result

print(solution())