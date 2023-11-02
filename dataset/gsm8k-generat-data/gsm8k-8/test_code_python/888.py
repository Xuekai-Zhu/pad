def solution():
    # Calculate the number of pets Teddy has
    teddy_dogs = 7
    teddy_cats = 8
    teddy_pets = teddy_dogs + teddy_cats

    # Calculate the number of pets Ben has
    ben_dogs = teddy_dogs + 9
    ben_cats = teddy_cats
    ben_pets = ben_dogs + ben_cats

    # Calculate the number of pets Dave has
    dave_dogs = teddy_dogs - 5
    dave_cats = teddy_cats + 13
    dave_pets = dave_dogs + dave_cats

    # Calculate the total number of pets
    total_pets = teddy_pets + ben_pets + dave_pets
    result = total_pets
    return result

print(solution())