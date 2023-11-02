def solution():
    """There are 88 dogs in a park. 12 of the dogs are running. Half of them are playing with toys. A fourth of them are barking. How many dogs are not doing anything?"""
    total_dogs = 88
    running_dogs = 12
    playing_dogs = total_dogs / 2
    barking_dogs = total_dogs / 4
    not_doing_anything = total_dogs - running_dogs - playing_dogs - barking_dogs
    result = not_doing_anything
    
    return result

print(solution())