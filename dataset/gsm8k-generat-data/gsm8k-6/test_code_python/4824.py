def solution():
    # Calculate the number of dogs not doing anything in the park
    running_dogs = 12
    playing_dogs = (1/2) * 88
    barking_dogs = (1/4) * 88
    not_doing_anything = 88 - running_dogs - playing_dogs - barking_dogs
    result = not_doing_anything
    return result

print(solution())