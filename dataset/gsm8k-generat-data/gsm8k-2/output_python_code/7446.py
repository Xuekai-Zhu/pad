def solution():
    """There are 15 cats in a shelter. One-third were adopted, and were replaced with twice the amount that were adopted. Later on, twice as many dogs showed up as there are cats. How many total animals are there in the shelter?"""
    num_cats = 15
    adopted_cats = num_cats // 3
    remaining_cats = num_cats - adopted_cats
    new_cats = adopted_cats * 2
    total_cats = remaining_cats + new_cats
    num_dogs = 2 * num_cats
    total_animals = total_cats + num_dogs
    result = total_animals
    return result

print(solution())