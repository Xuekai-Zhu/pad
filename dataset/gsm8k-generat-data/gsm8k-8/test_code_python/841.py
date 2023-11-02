def solution():
    # Define the ratio of dogs to cats
    dog_to_cat_ratio = 10/17

    # Calculate the total number of pets
    total_pets = 189

    # Calculate the number of dogs and cats
    total_ratio = 10 + 17
    total_dogs = int((10/total_ratio) * total_pets)
    total_cats = int((17/total_ratio) * total_pets)

    # Calculate the remaining number of dogs after giving 10 to Janet
    remaining_dogs = total_dogs - 10
    result = remaining_dogs
    return result

print(solution())