def solution():
    # Calculate the number of dogs and cats before giving away 10 dogs
    total_pets = 189
    dog_ratio = 10 / 27  # ratio of dogs to total pets
    cat_ratio = 17 / 27  # ratio of cats to total pets
    total_dogs = dog_ratio * total_pets
    total_cats = cat_ratio * total_pets

    # Calculate the number of dogs Heloise has left after giving away 10 dogs
    remaining_dogs = total_dogs - 10
    result = remaining_dogs
    return result

print(solution())