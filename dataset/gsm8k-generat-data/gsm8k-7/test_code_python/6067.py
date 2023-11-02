def solution():
    total_pets = 36
    dog_percent = 0.25
    cat_percent = 0.50

    # Calculate the number of dogs
    num_dogs = total_pets * dog_percent

    # Calculate the number of cats
    num_cats = total_pets * cat_percent

    # Calculate the number of bunnies
    num_bunnies = total_pets - num_dogs - num_cats
    result = num_bunnies
    return result

print(solution())