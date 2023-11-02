def solution():
    # Calculate the number of cats adopted
    cats_adopted = 15/3

    # Calculate the number of cats replaced
    cats_replaced = cats_adopted * 2

    # Calculate the total number of cats
    total_cats = 15 - cats_adopted + cats_replaced

    # Calculate the number of dogs
    dogs = total_cats * 2

    # Calculate the total number of animals
    total_animals = total_cats + dogs
    result = total_animals
    return result

print(solution())