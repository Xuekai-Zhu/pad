def solution():
    """In a community of 50 families, 15 families own 2 dogs, 20 families own 1 dog, while the remaining families own 2 cats each. How many dogs and cats are there in all?"""
    # Define the number of families and the number of dogs and cats per family
    num_families = 50
    dogs_per_family = 0
    cats_per_family = 2

    # Calculate the number of families with 2 dogs
    num_families_2dogs = 15

    # Calculate the number of families with 1 dog
    num_families_1dog = 20

    # Calculate the number of families with 2 cats
    num_families_2cats = num_families - num_families_2dogs - num_families_1dog

    # Calculate the total number of dogs and cats
    total_dogs = num_families_2dogs * 2 + num_families_1dog
    total_cats = num_families_2cats * 2

    # return the result as a tuple of (total_dogs, total_cats)
    result = (total_dogs, total_cats)
    return result

print(solution())