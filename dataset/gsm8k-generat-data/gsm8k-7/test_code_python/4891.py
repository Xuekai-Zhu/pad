def solution():
    num_dogs = 20
    dog_cost = 60

    num_cats = 60
    cat_cost = 40

    # Calculate the total cost of treating all dogs
    total_dog_cost = num_dogs * dog_cost

    # Calculate the total cost of treating all cats
    total_cat_cost = num_cats * cat_cost

    # Calculate the total cost of all animals
    total_cost = total_dog_cost + total_cat_cost
    result = total_cost
    return result

print(solution())