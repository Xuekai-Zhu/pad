def solution():
    # Find the number of pets each person has
    teddy_dogs = 7
    teddy_cats = 8
    ben_dogs = teddy_dogs + 9
    ben_cats = teddy_cats
    dave_dogs = teddy_dogs - 5
    dave_cats = teddy_cats + 13
    
    # Calculate the total number of pets
    total_pets = teddy_dogs + teddy_cats + ben_dogs + ben_cats + dave_dogs + dave_cats
    result = total_pets
    return result

print(solution())