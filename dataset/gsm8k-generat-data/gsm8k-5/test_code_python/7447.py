def solution():
    cats_in_shelter = 15  # There are 15 cats in the shelter

    # Calculate the number of cats that were adopted and replaced
    cats_adopted = cats_in_shelter // 3
    cats_replaced = 2 * cats_adopted

    # Calculate the number of cats currently in the shelter
    cats_in_shelter = cats_in_shelter - cats_adopted + cats_replaced

    # Calculate the number of dogs that showed up
    dogs_in_shelter = 2 * cats_in_shelter

    # Calculate the total number of animals in the shelter
    total_animals = cats_in_shelter + dogs_in_shelter
    result = total_animals
    return result

print(solution())