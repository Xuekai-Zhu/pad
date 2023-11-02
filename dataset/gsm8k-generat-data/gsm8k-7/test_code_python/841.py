def solution():
    total_pets = 189
    dog_cat_ratio = 10 + 17  # Ratio of dogs to cats
    num_dogs = 10/27 * total_pets  # Calculate the number of dogs
    num_cats = 17/27 * total_pets  # Calculate the number of cats

    # Subtract 10 from the number of dogs remaining with Heloise
    num_dogs_remaining = num_dogs - 10
    result = num_dogs_remaining
    return result

print(solution())