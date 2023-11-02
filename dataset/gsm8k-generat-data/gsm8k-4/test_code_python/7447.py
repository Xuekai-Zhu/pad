def solution():
    """There are 15 cats in a shelter. One-third were adopted, and were replaced with twice the amount that were adopted. Later on, twice as many dogs showed up as there are cats. How many total animals are there in the shelter?"""
    # Define the initial number of cats
    num_cats = 15

    # Calculate the number of cats adopted and replaced
    num_adopted = num_cats // 3
    num_replaced = num_adopted * 2
    num_cats = num_cats - num_adopted + num_replaced

    # Calculate the number of dogs
    num_dogs = num_cats * 2

    # Calculate the total number of animals
    total_animals = num_cats + num_dogs

    # return the result
    result = total_animals
    return result

print(solution())