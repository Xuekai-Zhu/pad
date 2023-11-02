def solution():
    # Calculate the number of cats Anthony has
    cats = (2/3) * 12

    # Calculate the number of dogs Anthony has
    dogs = 12 - cats

    # Calculate the number of cats Leonel has
    leonel_cats = 0.5 * cats

    # Calculate the number of dogs Leonel has
    leonel_dogs = dogs + 7

    # Calculate the total number of animals
    total_animals = cats + dogs + leonel_cats + leonel_dogs
    result = total_animals
    return result

print(solution())