def solution():
    dogs_grooming_time = 2.5 * 60  # convert hours to minutes
    cats_grooming_time = 0.5 * 60  # convert hours to minutes
    num_dogs = 5
    num_cats = 3

    # Calculate the total grooming time for all dogs
    total_dog_grooming_time = dogs_grooming_time * num_dogs

    # Calculate the total grooming time for all cats
    total_cat_grooming_time = cats_grooming_time * num_cats

    # Calculate the total grooming time for all animals
    total_grooming_time = total_dog_grooming_time + total_cat_grooming_time

    result = total_grooming_time
    return result

print(solution())