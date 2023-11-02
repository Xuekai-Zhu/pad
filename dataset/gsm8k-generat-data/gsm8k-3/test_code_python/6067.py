def solution():
    """Michael has 36 pets. 25% of them are dogs, 50% are cats, and the rest are bunnies. How many bunnies does he have?"""
    # Define the total number of pets
    total_pets = 36

    # Calculate the number of dogs
    num_dogs = total_pets * 0.25

    # Calculate the number of cats
    num_cats = total_pets * 0.5

    # Calculate the number of bunnies
    num_bunnies = total_pets - num_dogs - num_cats

    # Display the number of bunnies
    result = num_bunnies
    return result

print(solution())