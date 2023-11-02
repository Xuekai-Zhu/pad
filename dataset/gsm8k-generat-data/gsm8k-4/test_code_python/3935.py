def solution():
    """Karen works at an animal shelter with 30 dogs, 28 cats, and 20 lizards. Every month, 50% of the dogs are adopted, 25% of the cats are adopted, and 20% of lizards are adopted. If the shelter takes in 13 new pets a month, how many pets are there after one month?"""
    # Define the initial number of pets
    num_dogs = 30
    num_cats = 28
    num_lizards = 20

    # Calculate the number of pets that get adopted
    adopted_dogs = num_dogs * 0.5
    adopted_cats = num_cats * 0.25
    adopted_lizards = num_lizards * 0.2

    # Subtract the number of adopted pets from the initial number of pets
    num_dogs -= adopted_dogs
    num_cats -= adopted_cats
    num_lizards -= adopted_lizards

    # Add the new pets to the number of remaining pets
    num_dogs += 4
    num_cats += 4
    num_lizards += 5

    # Calculate the total number of pets
    total_pets = num_dogs + num_cats + num_lizards

    # Return the result
    result = total_pets
    return result

print(solution())