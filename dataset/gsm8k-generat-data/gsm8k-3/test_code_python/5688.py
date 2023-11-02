def solution():
    """In a classroom there are 30 students. 1/3 of them are boys. Among the girls, 40% own dogs, 20% own a cat, and the rest have no pets. How many girls in the class have no pet?"""
    # Calculate the number of boys
    num_boys = 30 // 3

    # Calculate the number of girls
    num_girls = 30 - num_boys

    # Calculate the number of girls who own dogs
    num_girls_dogs = int(num_girls * 0.4)

    # Calculate the number of girls who own cats
    num_girls_cats = int(num_girls * 0.2)

    # Calculate the number of girls who have no pets
    num_girls_no_pets = num_girls - num_girls_dogs - num_girls_cats

    # Display the number of girls with no pets
    result = num_girls_no_pets
    return result

print(solution())