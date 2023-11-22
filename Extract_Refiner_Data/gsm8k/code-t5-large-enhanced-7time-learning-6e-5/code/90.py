def solution():
    
    # Define the number of dogs and cats
    num_dogs = 60
    num_cats = num_dogs * 2

    # Calculate the combined number of pet dogs and cats
    total_pets = num_dogs + num_cats

    # Calculate the number of rabbits pets
    num_rabbits_pets = total_pets - 12

    # return the result
    result = num_rabbits_pets
    return result

print(solution())