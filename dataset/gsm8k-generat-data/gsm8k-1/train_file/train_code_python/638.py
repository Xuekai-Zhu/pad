def solution():
    """In a community of 50 families, 15 families own 2 dogs, 20 families own 1 dog, while the remaining families own 2 cats each. How many dogs and cats are there in all?"""
    num_families = 50
    num_dogs = (15 * 2) + 20
    num_cats = (num_families - 15 - 20) * 2
    total_animals = num_dogs + num_cats
    result = (num_dogs, num_cats, total_animals)
    return result

print(solution())