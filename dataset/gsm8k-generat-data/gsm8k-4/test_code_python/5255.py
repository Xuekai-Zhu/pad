def solution():
    """Phoebe has two pizzas to share with her and three friends. One has pepperoni and the other has cheese. They both have 16 slices. They all eat the same amount. One friend eats only pepperoni, while the rest have an equal number of slices of each. At the end, there is one slice of pepperoni left and 7 slices of cheese, how many slices does each person eat?"""
    # Define the number of pizzas and the number of slices per pizza
    num_pizzas = 2
    slices_per_pizza = 16

    # Calculate the total number of slices
    total_slices = num_pizzas * slices_per_pizza

    # Calculate the number of slices of pepperoni pizza
    pepperoni_slices = total_slices - 7 - 1

    # Calculate the number of friends who eat both pizza types
    num_friends_both = 3 - 1

    # Calculate the number of slices per person
    slices_per_person = (pepperoni_slices + 8) / 4

    # Return the result
    result = slices_per_person
    return result

print(solution())