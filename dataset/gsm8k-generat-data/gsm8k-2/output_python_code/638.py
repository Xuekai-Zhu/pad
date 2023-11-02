def solution():
    """In a community of 50 families, 15 families own 2 dogs, 20 families own 1 dog, while the remaining families own 2 cats each. How many dogs and cats are there in all?"""
    total_families = 50
    two_dog_families = 15
    one_dog_families = 20
    two_cat_families = total_families - two_dog_families - one_dog_families
    total_dogs = (2 * two_dog_families) + one_dog_families
    total_cats = 2 * two_cat_families
    result = (total_dogs, total_cats)
    return result

print(solution())