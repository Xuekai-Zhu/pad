def solution():
    
    # Define the number of cats
    cats = 3

    # Define the number of dogs
    dogs = cats * 3

    # Define the number of rabbits
    rabbits = dogs - 2

    # Define the number of fish
    fish = rabbits * 3

    # Define the number of gerbils
    gerbils = fish / 3

    # Calculate the total number of pets
    total_pets = cats + dogs + rabbits + fish + gerbils

    # Display the total number of pets
    result = total_pets
    return result

print(solution())