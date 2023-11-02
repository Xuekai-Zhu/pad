def solution():
    """Phoebe has two pizzas to share with her and three friends. One has pepperoni and the other has cheese. They both have 16 slices. They all eat the same amount. One friend eats only pepperoni, while the rest have an equal number of slices of each. At the end, there is one slice of pepperoni left and 7 slices of cheese, how many slices does each person eat?"""
    total_slices = 16 * 2
    slices_left = 1 + 7
    slices_eaten = total_slices - slices_left
    num_friends = 3
    pepperoni_slices = 1
    cheese_slices = (slices_eaten - pepperoni_slices) / (num_friends - 1)
    total_slices_per_person = pepperoni_slices + cheese_slices
    result = total_slices_per_person
    return result

print(solution())