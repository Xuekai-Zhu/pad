def solution():
    total_families = 50  # There are 50 families in the community
    dog_owners_2 = 15  # 15 families own 2 dogs each
    dog_owners_1 = 20  # 20 families own 1 dog each

    # Calculate the total number of dogs in the community
    total_dogs = (dog_owners_2 * 2) + dog_owners_1

    # Calculate the total number of cats in the community
    total_cats = (total_families - dog_owners_2 - dog_owners_1) * 2

    # Calculate the total number of dogs and cats in the community
    total_animals = total_dogs + total_cats
    result = total_animals
    return result

print(solution())