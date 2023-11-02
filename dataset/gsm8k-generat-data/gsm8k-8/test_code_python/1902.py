def solution():
    # Define the number of antelopes
    antelopes = 80

    # Calculate the number of rabbits
    rabbits = antelopes + 34

    # Calculate the total number of antelopes and rabbits
    total_antelopes_rabbits = antelopes + rabbits

    # Calculate the number of hyenas
    hyenas = total_antelopes_rabbits - 42

    # Calculate the number of wild dogs
    wild_dogs = hyenas + 50

    # Calculate the number of leopards
    leopards = rabbits / 2

    # Calculate the total number of animals
    total_animals = antelopes + rabbits + hyenas + wild_dogs + leopards

    result = total_animals
    return result

print(solution())