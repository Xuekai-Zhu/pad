def solution():
    """Dean ordered 2 large pizzas that were each cut into 12 slices. His friends Frank and Sammy came over to enjoy some pizza and watch a movie. Dean was hungry and ate half of the Hawaiian pizza. Frank only ate 3 slices of Hawaiian pizza and Sammy ate a third of the cheese pizza. How many total slices were left over?"""
    # Define the number of pizzas and slices per pizza
    pizzas = 2
    slices_per_pizza = 12

    # Calculate the total number of slices
    total_slices = pizzas * slices_per_pizza

    # Calculate the number of slices of Hawaiian pizza that Dean ate
    dean_hawaiian = slices_per_pizza / 2

    # Calculate the number of slices of Hawaiian pizza that Frank ate
    frank_hawaiian = 3

    # Calculate the number of slices of cheese pizza that Sammy ate
    sammy_cheese = slices_per_pizza / 3

    # Calculate the total number of slices eaten
    total_eaten = dean_hawaiian + frank_hawaiian + sammy_cheese

    # Calculate the number of slices left over
    slices_left = total_slices - total_eaten

    result = slices_left
    return result

print(solution())