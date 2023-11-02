def solution():
    # Calculate the number of families that own 2 cats each
    cat_families = 50 - 15 - 20

    # Calculate the total number of cats owned by these families
    total_cats = 2 * cat_families

    # Calculate the total number of dogs owned by the first 15 families
    dogs_from_2dog_families = 2 * 15

    # Calculate the total number of dogs owned by the 20 families with 1 dog each
    dogs_from_1dog_families = 20

    # Calculate the total number of dogs in the community
    total_dogs = dogs_from_2dog_families + dogs_from_1dog_families

    # Calculate the total number of animals in the community
    total_animals = total_cats + total_dogs

    result = (total_dogs, total_cats, total_animals)
    return result

print(solution())