def solution():
    """Phoebe has two pizzas to share with her and three friends. One has pepperoni and the other has cheese. They both have 16 slices. They all eat the same amount. One friend eats only pepperoni, while the rest have an equal number of slices of each. At the end, there is one slice of pepperoni left and 7 slices of cheese, how many slices does each person eat?"""
    pepperoni_slices = 15
    cheese_slices = 16 - 7
    total_people = 4
    equal_slices_per_person = (pepperoni_slices + cheese_slices) / (total_people - 1)
    pepperoni_eater_slices = pepperoni_slices - equal_slices_per_person
    result = equal_slices_per_person
    return result

print(solution())