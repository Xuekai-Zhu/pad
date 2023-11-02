def solution():
    total_families = 50
    num_families_with_2_dogs = 15
    num_families_with_1_dog = 20

    # Calculate the number of families with 2 cats
    num_families_with_2_cats = total_families - num_families_with_2_dogs - num_families_with_1_dog

    # Calculate the total number of dogs
    total_dogs = (num_families_with_2_dogs * 2) + num_families_with_1_dog

    # Calculate the total number of cats
    total_cats = num_families_with_2_cats * 2

    # Calculate the total number of dogs and cats
    total_animals = total_dogs + total_cats
    result = (total_dogs, total_cats, total_animals)
    return result

print(solution())