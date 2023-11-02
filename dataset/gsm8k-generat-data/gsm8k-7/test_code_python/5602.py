def solution():
    initial_num_cats = 28
    initial_num_dogs = 18
    cats_to_adoption = 3

    # Calculate the new number of cats after giving some up for adoption
    num_cats = initial_num_cats - cats_to_adoption

    # Calculate the difference between the new number of cats and the initial number of dogs
    cat_dog_diff = num_cats - initial_num_dogs
    result = cat_dog_diff
    return result

print(solution())