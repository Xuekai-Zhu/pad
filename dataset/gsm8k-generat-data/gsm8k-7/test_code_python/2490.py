def solution():
    num_dogs = 6
    num_cats = num_dogs / 2
    num_birds = num_dogs * 2
    num_fish = num_dogs * 3

    # Calculate the total number of animals for sale
    total_animals = num_dogs + num_cats + num_birds + num_fish
    result = total_animals
    return result

print(solution())