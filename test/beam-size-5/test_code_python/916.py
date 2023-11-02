def solution():
    num_cats = 3
    num_dogs = num_cats * 3
    num_rabbits = num_dogs - 2
    num_fish_tank = num_rabbits * 3
    num_gerbils = num_fish_tank / 3

    # Calculate the total number of pets Larry has
    total_pets = num_cats + num_dogs + num_rabbits + num_gerbils
    result = total_pets
    return result

print(solution())