def solution():
    """Michael has 36 pets. 25% of them are dogs, 50% are cats, and the rest are bunnies. How many bunnies does he have?"""
    # Define the total number of pets and the percentage of dogs and cats
    total_pets = 36
    percent_dogs = 0.25
    percent_cats = 0.5

    # Calculate the number of dogs and cats
    num_dogs = total_pets * percent_dogs
    num_cats = total_pets * percent_cats

    # Calculate the number of bunnies
    num_bunnies = total_pets - num_dogs - num_cats

    # return the result
    result = num_bunnies
    return result

print(solution())