def solution():
    total_animals = 300
    cat_ratio = 2/3
    dog_ratio = 1/3

    # Calculate the number of cats
    num_cats = total_animals * cat_ratio

    # Calculate the number of dogs
    num_dogs = total_animals * dog_ratio

    # Calculate the total number of dog legs
    total_dog_legs = num_dogs * 4

    result = total_dog_legs
    return result

print(solution())