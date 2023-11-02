def solution():
    num_dogs = 88
    running_dogs = 12
    playing_dogs = num_dogs / 2
    barking_dogs = num_dogs / 4

    # Calculate the total number of dogs that are not doing anything
    num_not_doing_anything = num_dogs - running_dogs - playing_dogs - barking_dogs
    result = num_not_doing_anything
    return result

print(solution())