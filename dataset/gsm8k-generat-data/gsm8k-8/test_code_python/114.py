def solution():
    # Define the number of dogs and cats
    num_dogs = 2
    num_cats = 3

    # Calculate the total number of dogs and cats
    total_dogs_cats = num_dogs + num_cats

    # Calculate the number of fish
    num_fish = 2 * total_dogs_cats

    # Calculate the total number of pets
    total_pets = num_dogs + num_cats + num_fish
    result = total_pets
    return result

print(solution())