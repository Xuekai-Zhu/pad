def solution():
    # Find the number of dogs
    num_dogs = 184 / 2 

    # Calculate the number of cows to be sold
    cows_to_be_sold = 184 / 4

    # Calculate the number of dogs to be sold
    dogs_to_be_sold = num_dogs * 3 / 4

    # Calculate the number of animals remaining on the farm
    remaining_animals = 184 - cows_to_be_sold + num_dogs - dogs_to_be_sold

    result = remaining_animals
    return result

print(solution())