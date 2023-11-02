def solution():
    teddy_dogs = 7
    teddy_cats = 8

    ben_dogs = teddy_dogs + 9
    ben_cats = teddy_cats

    dave_dogs = teddy_dogs - 5
    dave_cats = teddy_cats + 13

    # Calculate the total number of dogs and cats
    total_dogs = teddy_dogs + ben_dogs + dave_dogs
    total_cats = teddy_cats + ben_cats + dave_cats

    # Calculate the total number of pets
    total_pets = total_dogs + total_cats
    result = total_pets
    return result

print(solution())