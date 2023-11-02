def solution():
    """There are 15 cats in a shelter. One-third were adopted, and were replaced with twice the amount that were adopted. Later on, twice as many dogs showed up as there are cats. How many total animals are there in the shelter?"""
    # Define the initial number of cats and calculate the number adopted
    num_cats = 15
    num_adopted_cats = num_cats // 3

    # Calculate the number of cats remaining in the shelter after adoptions
    num_cats_remaining = num_cats - num_adopted_cats

    # Calculate the number of cats that were brought in as replacements
    num_new_cats = num_adopted_cats * 2

    # Calculate the total number of cats in the shelter after replacements
    total_cats = num_cats_remaining + num_new_cats

    # Calculate the number of dogs that showed up
    num_dogs = total_cats * 2

    # Calculate the total number of animals in the shelter
    total_animals = total_cats + num_dogs

    # Display the total number of animals in the shelter
    result = total_animals
    return result

print(solution())