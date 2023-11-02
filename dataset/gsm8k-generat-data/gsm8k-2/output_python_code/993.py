def solution():
    """Dean ordered 2 large pizzas that were each cut into 12 slices. His friends Frank and Sammy came over to enjoy some pizza and watch a movie. Dean was hungry and ate half of the Hawaiian pizza. Frank only ate 3 slices of Hawaiian pizza and Sammy ate a third of the cheese pizza. How many total slices were left over?"""
    total_slices = 2 * 12
    hawaiian_slices = total_slices // 2
    frank_hawaiian_slices = 3
    cheese_slices = total_slices - hawaiian_slices
    sammy_cheese_slices = cheese_slices // 3
    leftovers = total_slices - (hawaiian_slices - frank_hawaiian_slices) - (cheese_slices - sammy_cheese_slices)
    result = leftovers
    return result

print(solution())