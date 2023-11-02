def solution():
    """In a classroom there are 30 students. 1/3 of them are boys. Among the girls, 40% own dogs, 20% own a cat, and the rest have no pets. How many girls in the class have no pet?"""
    # Calculate the number of boys and girls
    total_students = 30
    boys = total_students // 3
    girls = total_students - boys

    # Calculate the number of girls who own dogs and cats
    dog_owners = 0.4 * girls
    cat_owners = 0.2 * girls

    # Calculate the number of girls who don't have pets
    no_pets = girls - dog_owners - cat_owners

    result = no_pets
    return result

print(solution())