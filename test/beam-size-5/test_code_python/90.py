def solution():
    
    # Define the number of dogs and cats
    dogs = 60
    cats = 2 * dogs

    # Calculate the combined number of pet dogs and cats
    pet_dogs_and_cats = dogs + cats

    # Calculate the number of rabbits pets
    rabbits_pets = pet_dogs_and_cats - 12

    # Calculate the total number of pets
    total_pets = pet_dogs_and_cats + rabbits_pets

    # Display the total number of pets
    result = total_pets
    return result

print(solution())