def solution():
    """There are 15 cats in a shelter. One-third were adopted, and were replaced with twice the amount that were adopted. Later on, twice as many dogs showed up as there are cats. How many total animals are there in the shelter?"""
    initial_cats = 15
    cats_adopted = initial_cats // 3
    cats_replaced = cats_adopted * 2
    remaining_cats = initial_cats - cats_adopted + cats_replaced
    dogs = remaining_cats * 2
    total_animals = remaining_cats + dogs
    result = total_animals
    return result

print(solution())