def solution():
    # Calculate the number of boys in the class
    num_boys = 30 * (1/3)

    # Calculate the number of girls in the class
    num_girls = 30 - num_boys

    # Calculate the number of girls who own a dog
    dog_owners = num_girls * 0.4

    # Calculate the number of girls who own a cat
    cat_owners = num_girls * 0.2

    # Calculate the number of girls who have no pets
    no_pet_owners = num_girls - dog_owners - cat_owners

    result = no_pet_owners
    return result

print(solution())