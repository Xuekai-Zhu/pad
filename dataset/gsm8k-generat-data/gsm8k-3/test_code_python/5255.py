def solution():
    """Phoebe has two pizzas to share with her and three friends. One has pepperoni and the other has cheese. They both have 16 slices. They all eat the same amount. One friend eats only pepperoni, while the rest have an equal number of slices of each. At the end, there is one slice of pepperoni left and 7 slices of cheese, how many slices does each person eat?"""
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 16

    # Define the number of friends
    num_friends = 3

    # Calculate the total number of slices eaten by all friends
    total_slices_eaten = (num_friends - 1) * ((SLICES_PER_PIZZA - 1) / 2) + ((SLICES_PER_PIZZA - 7) / 2)

    # Calculate the number of slices each person eats
    slices_per_person = total_slices_eaten / num_friends

    # Display the number of slices each person eats
    result = slices_per_person
    return result

print(solution())