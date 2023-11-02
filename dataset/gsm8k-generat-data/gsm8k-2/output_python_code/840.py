def solution():
    """Heloise has dogs and cats in the ratio of 10:17, with the total number of pets being 189. If she gives 10 dogs to her friend Janet, how many dogs does she remain with altogether?"""
    total_pets = 189
    dog_ratio = 10/27
    cat_ratio = 17/27
    total_dogs = dog_ratio * total_pets
    remaining_dogs = total_dogs - 10
    result = remaining_dogs
    return result

print(solution())