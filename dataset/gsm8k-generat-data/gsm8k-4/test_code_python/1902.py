def solution():
    """Josie and her family went on a safari and had an exciting time watching different animals grazing and playing together. She decided to count each animal she saw and calculated their total number. She counted 80 antelopes, 34 more rabbits than antelopes, 42 fewer hyenas than the total number of antelopes and rabbits combined, 50 more wild dogs than hyenas, and the number of leopards was half the number of rabbits. What the total number of animals that Josie counted?"""
    # Calculate the number of rabbits
    rabbits = 80 + 34

    # Calculate the total number of antelopes and rabbits
    antelopes_rabbits_total = 80 + rabbits

    # Calculate the number of hyenas
    hyenas = antelopes_rabbits_total - 42

    # Calculate the number of wild dogs
    wild_dogs = hyenas + 50

    # Calculate the number of leopards
    leopards = rabbits / 2

    # Calculate the total number of animals
    total_animals = antelopes_rabbits_total + hyenas + wild_dogs + leopards

    # return the result
    result = total_animals
    return result

print(solution())