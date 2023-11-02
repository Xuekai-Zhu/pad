def solution():
    """Karen works at an animal shelter with 30 dogs, 28 cats, and 20 lizards. Every month, 50% of the dogs are adopted, 25% of the cats are adopted, and 20% of lizards are adopted. If the shelter takes in 13 new pets a month, how many pets are there after one month?"""
    # Define the number of animals at the shelter
    DOGS = 30
    CATS = 28
    LIZARDS = 20
    NEW_PETS = 13

    # Calculate the number of animals adopted
    dogs_adopted = DOGS * 0.5
    cats_adopted = CATS * 0.25
    lizards_adopted = LIZARDS * 0.2

    # Calculate the number of animals remaining
    dogs_remaining = DOGS - dogs_adopted
    cats_remaining = CATS - cats_adopted
    lizards_remaining = LIZARDS - lizards_adopted

    # Calculate the total number of animals
    total_animals = dogs_remaining + cats_remaining + lizards_remaining + NEW_PETS

    # Display the total number of animals
    result = total_animals
    return result

print(solution())