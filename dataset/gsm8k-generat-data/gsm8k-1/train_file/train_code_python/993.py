def solution():
    """Dean ordered 2 large pizzas that were each cut into 12 slices. His friends Frank and Sammy came over to enjoy some pizza and watch a movie. Dean was hungry and ate half of the Hawaiian pizza. Frank only ate 3 slices of Hawaiian pizza and Sammy ate a third of the cheese pizza. How many total slices were left over?"""
    num_pizzas = 2
    slices_per_pizza = 12
    total_slices = num_pizzas * slices_per_pizza
    hawaiian_slices = int((slices_per_pizza/2) * num_pizzas)
    left_hawaiian_slices = hawaiian_slices - (slices_per_pizza/2)
    frank_hawaiian_slices = 3
    cheese_slices = slices_per_pizza * num_pizzas
    sammy_cheese_slices = int(cheese_slices/3)
    total_eaten_slices = hawaiian_slices + cheese_slices - left_hawaiian_slices - frank_hawaiian_slices - sammy_cheese_slices
    left_over_slices = total_slices - total_eaten_slices
    result = left_over_slices
    return result

print(solution())