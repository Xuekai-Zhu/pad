def solution():
    # Define the initial number of cats and dogs
    initial_cats = 28
    initial_dogs = 18

    # Subtract the number of cats given up for adoption
    current_cats = initial_cats - 3

    # Calculate the difference between current cats and dogs
    cat_dog_difference = current_cats - initial_dogs
    result = cat_dog_difference
    return result

print(solution())