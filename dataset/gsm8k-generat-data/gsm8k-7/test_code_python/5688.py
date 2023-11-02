def solution():
    total_students = 30
    boys_fraction = 1/3

    # Calculate the number of boys in the class
    num_boys = total_students * boys_fraction

    # Calculate the number of girls in the class
    num_girls = total_students - num_boys

    # Calculate the number of girls who own dogs
    num_dog_owners = 0.4 * num_girls

    # Calculate the number of girls who own cats
    num_cat_owners = 0.2 * num_girls

    # Calculate the number of girls who have no pets
    num_no_pets = num_girls - num_dog_owners - num_cat_owners
    result = num_no_pets
    return result

print(solution())