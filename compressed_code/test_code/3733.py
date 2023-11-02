def solution():
    
    total_dogs = 88
    running_dogs = 12
    playing_dogs = total_dogs / 2
    barking_dogs = total_dogs / 4
    not_doing_anything = total_dogs - running_dogs - playing_dogs - barking_dogs
    result = not_doing_anything
    return result

print(solution())