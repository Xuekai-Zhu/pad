def solution():
    total_dogs = 88  # There are 88 dogs in the park
    running_dogs = 12  # 12 dogs are running
    playing_dogs = total_dogs / 2  # Half of the dogs are playing
    barking_dogs = total_dogs / 4  # A fourth of the dogs are barking

    # Calculate the number of dogs not doing anything
    dogs_not_doing_anything = total_dogs - (running_dogs + playing_dogs + barking_dogs)
    result = dogs_not_doing_anything
    return result

print(solution())