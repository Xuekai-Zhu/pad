def solution():
    # Find the number of boys in the class
    boys = 30 // 3

    # Find the number of girls in the class
    girls = 30 - boys

    # Find the number of girls who own dogs
    girls_with_dog = int(0.4 * girls)

    # Find the number of girls who own cats
    girls_with_cat = int(0.2 * girls)

    # Find the number of girls who have no pets
    girls_with_no_pet = girls - girls_with_dog - girls_with_cat

    result = girls_with_no_pet
    return result

print(solution())