def solution():
    num_cats = 2
    cat_cost = 50

    num_adult_dogs = 3
    adult_dog_cost = 100

    num_puppies = 2
    puppy_cost = 150

    # Calculate total cost for cats
    cat_total = num_cats * cat_cost

    # Calculate total cost for adult dogs
    adult_dog_total = num_adult_dogs * adult_dog_cost

    # Calculate total cost for puppies
    puppy_total = num_puppies * puppy_cost

    # Calculate total cost for all animals
    total_cost = cat_total + adult_dog_total + puppy_total
    result = total_cost
    return result

print(solution())